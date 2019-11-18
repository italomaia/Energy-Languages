#!/usr/bin/env python3
import os

from subprocess import check_output
from lazyme.string import color_print
from typing import List

PATH = os.path.abspath(os.path.dirname('.'))


def make_root(name):
    return os.path.join(PATH, name)


def _build_docker_image(root, image_name):
    args = ["docker", "build", "-t", image_name, "."]
    output = check_output(args, cwd=root).decode('utf-8')
    print(output)


def build_docker_image(name, base_image=None):
    image_name = make_docker_image_name(name)

    if not docker_image_exists(image_name):
        # docker folder root
        root = make_root(name)
        _build_docker_image(root, image_name)

    return image_name


def make_docker_image_name(name):
    return f"energy/{name}:1"


def run_docker_image(image_name: str, action: str):
    check_output(["docker", 'run', image_name, "/usr/bin/python3 compile_all.py %s" % action])


def docker_image_exists(image):
    return len(check_output(["docker", "images", "-q", image])) > 0


def run_command(name):
    pass


def clean_command(name):
    pass


def measure_command(name):
    pass


def file_exists(file_path):
    return os.path.isfile(file_path) if file_path else False


def main(lang_list: List[str], action: str):
    # builds base image for all other images
    rapl_image_name = build_docker_image('rapl')  # noqa: F841

    for lang in lang_list:
        image_name = build_docker_image(lang.lower(), rapl_image_name)
        run_docker_image(image_name, action)


def make_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='If testing a language, be sure to build first')
    parser.add_argument('languages', nargs='+', help='languages to be used')
    parser.add_argument(
        '-a', '--act',
        required=True,
        choices=('mem', 'compile', 'run', 'measure'),
        help='action to execute'
    )

    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()

    color_print(f"Preparing to measure languages performance", color='yellow', bold=True)
    main(namespace.languages, namespace.act)
