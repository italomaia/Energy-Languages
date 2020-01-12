#!/usr/bin/env python3
import os
import subprocess

from lazyme.string import color_print
from typing import List

PATH = os.path.abspath(os.path.dirname('.'))


def make_root(name):
    return os.path.join(PATH, name)


def _build_docker_image(root, image_name):
    args = ["docker", "build", "-t", image_name, "."]
    output = subprocess.check_output(args, cwd=root).decode('utf-8')
    print(output)


def build_docker_image(name, force_build=False):
    image_name = make_docker_image_name(name)

    if force_build or not docker_image_exists(image_name):
        # docker folder root
        root = make_root(name)
        _build_docker_image(root, image_name)
        print("image %s built" % image_name)
    else:
        print("image %s was not built" % image_name)

    print("")
    return image_name


def make_docker_image_name(name):
    return f"energy/{name}:1"


def get_data_folder():
    return os.path.join(os.getcwd(), "data/")


def get_result_folder():
    return os.path.join(os.getcwd(), "result/")


def run_docker_image(image_name: str, action: str):
    data_folder = get_data_folder()
    result_folder = get_result_folder()
    cmd = [
        "docker", 'run', '--rm',
        "-v", "%s:/root/data/" % data_folder,
        "-v", "%s:/opt/result/" % result_folder,
        image_name, "/usr/bin/python3", "compile_all.py", action
    ]

    print("running: " + ' '.join(cmd))

    prc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        bufsize=1,
        universal_newlines=True
    )

    while prc.poll() is None:
        for line in prc.stdout:
            print(line)


def docker_image_exists(image):
    return len(subprocess.check_output(["docker", "images", "-q", image])) > 0


def run_command(name):
    pass


def clean_command(name):
    pass


def measure_command(name):
    pass


def file_exists(file_path):
    return os.path.isfile(file_path) if file_path else False


def main(lang_list: List[str], action: str, force_build):
    # builds base image for all other images
    base_image_name = build_docker_image('base', force_build)  # noqa: F841

    for lang in lang_list:
        image_name = build_docker_image(lang.lower(), force_build)
        run_docker_image(image_name, action)


def make_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='If testing a language, be sure to build first')
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

    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()

    color_print(f"Preparing to measure languages performance", color='yellow', bold=True)
    main(namespace.languages, namespace.act, namespace.force_build)
