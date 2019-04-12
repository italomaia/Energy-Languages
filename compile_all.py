import sys
import os
from subprocess import call, Popen, PIPE
from lazyme.string import color_print
from typing import List, Optional

PATH = '.'
ACT_SET = set([
    'compile',
    'run',
    'clean',
    'measure',
])


def file_exists(file_path):
    if not file_path:
        return False
    else:
        return os.path.isfile(file_path)


def run_command(root, action):
    makefile = os.path.join(root, "Makefile")

    if file_exists(makefile):
        print('Checking ' + root)

        cmd = 'cd ' + root + '; make ' + action
        pipes = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
        std_out, std_err = pipes.communicate()

        if (action == 'compile') | (action == 'run'):
            if pipes.returncode != 0:
                # an error happened!
                err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
                color_print('[E] Error on ' + root + ': ', color='red', bold=True)
                print(err_msg)
            elif len(std_err):
                # return code is 0 (no error), but we may want to
                # do something with the info on std_err
                # i.e. logger.warning(std_err)
                color_print('[OK]', color='green')
            else:
                color_print('[OK]', color='green')
        if action == 'measure':
            call(['sleep', '5'])


def main(action: str, lang_list: Optional[List[str]]):
    lang_path_list: Optional[List[str]] = None

    if lang_list is not None:
        lang_path_list = [os.path.join(PATH, lang).lower() for lang in lang_list]

    for root, dirs, files in os.walk(PATH):
        if lang_path_list is not None:
            for lang_path in lang_path_list:
                if root.lower().startswith(lang_path):
                    run_command(root, action)


def make_parser():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='If testing a compiled language, be sure to compile first')
    parser.add_argument('acts', nargs='+', help='actions to be executed')
    parser.add_argument('-l', '--lang-list', nargs='+', default=None, required=False, help='languages to be used')

    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()

    for act in namespace.acts:
        if act in ACT_SET:
            color_print("Performing \"{act}\" action...", color='yellow', bold=True)
            main(act, namespace.lang_list)
        else:
            color_print(f"Error: Unrecognized action \"{act}\"", color='red')
            sys.exit(1)
