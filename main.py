#!/usr/bin/env python3
import os
from subprocess import check_output
from subprocess import PIPE
from subprocess import CalledProcessError
from subprocess import Popen

from lazyme.string import color_print
from typing import List

# current directory
CUR_DIR = os.path.abspath(os.path.dirname('.'))


def make_root(name):
    "Creates the filepath for a language folder"
    return os.path.join(CUR_DIR, name)


def _build_docker_image(dir_path: str, image_name: str):
    """Builds a docker image from given folder with given name.

    Arguments:
        dir_path {str} -- path to docker image
        image_name {str} -- target docker image name
    """
    args = ["docker", "build", "-t", image_name, "."]

    return check_output(
        args,
        cwd=dir_path,
        stderr=PIPE
    ).decode('utf-8').strip()  # nosec B603


def build_docker_image(name: str, force_build: bool = False):
    image_name = make_docker_image_name(name)

    if force_build or not docker_image_exists(image_name):
        # docker folder root
        root = make_root(name)
        print(_build_docker_image(root, image_name))
        print(f"image {image_name} built")
    else:
        print(f"image {image_name} was not built")

    print("")
    return image_name


def make_docker_image_name(name, version: int = 1):
    "Builds a docker image name"

    return f"energy/{name}:{version}"


def get_data_folder() -> str:
    return make_root("data")


def get_results_folder() -> str:
    return make_root("results")


def get_measures_folder() -> str:
    return make_root("measures")


def run_docker_image(image_name: str, action: str, only: str):
    """Runs whatever `action` is requested for the given image, that
    should already exist.

    Arguments:
        image_name {str} -- existing image name
        action {str} -- 'run' or 'measure'
    """
    data_folder = get_data_folder()
    results_folder = get_results_folder()
    measures_folder = get_measures_folder()

    options = []

    if only:
        options += ['-o', only]

    cmd = [
        'docker', 'run', '--rm', '-t',
        '-v', "%s:/root/data/" % data_folder,
        '-v', "%s:/opt/results/" % results_folder,
        '-v', "%s:/opt/measures/" % measures_folder,
        # -u allows us to see the output faster
        image_name, '/usr/bin/python3', '-u',
        'compile_all.py'
    ]

    cmd = cmd + options + ['prepare', 'compile', action]

    print("running: " + ' '.join(cmd), end='\n\n')

    prc = Popen(
        cmd,
        stdout=PIPE,
        universal_newlines=True
    )

    while prc.poll() is None:
        for line in prc.stdout:
            print(line)


def docker_image_exists(name: str) -> bool:
    "Checks if image `name` exists"
    return len(check_output(["docker", "images", "-q", name])) > 0


def run_command(name):
    pass


def clean_command(name):
    pass


def measure_command(name):
    pass


def file_exists(file_path):
    return os.path.isfile(file_path) if file_path else False


def main(
    lang_list: List[str],
    action: str,
    force_build: bool,
    only: str
) -> None:
    try:
        # builds base image used by all other images
        base_image_name = build_docker_image('base', force_build)  # noqa: F841
    except CalledProcessError as err:
        color_print(
            "Could not create base docker image",
            color="red", bold=True)

        raise err

    for lang in lang_list:
        try:
            image_name = build_docker_image(lang.lower(), force_build)
            run_docker_image(image_name, action, only)
        except CalledProcessError as err:
            out_msg = err.stdout.decode().strip()
            err_msg = err.stderr.decode().strip()
            err_code = err.returncode

            print(f"[M][{lang}] {out_msg}; Code {err_code}")
            print(f"[E][{lang}] {err_msg}; Code {err_code}")


def make_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(
        description='If testing a language, be sure to build first')
    parser.add_argument('languages', nargs='+', help='languages to be used')
    parser.add_argument(
        '-a', '--act',
        required=True,
        choices=('run', 'measure'),
        help='action to execute'
    )
    parser.add_argument(
        '-b', '--force-build',
        default=False,
        help='build docker images even if they already exist',
        action='store_true'
    )
    parser.add_argument(
        '-o', '--only',
        type=str,
        default=None,
        required=False,
        help='only run the requested test'
    )

    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()

    color_print(
        "Preparing to measure languages performance",
        color='yellow',
        bold=True)

    main(
        namespace.languages,
        namespace.act,
        namespace.force_build,
        namespace.only)
