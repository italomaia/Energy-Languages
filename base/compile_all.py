import os
import time
import argparse

from subprocess import call
from subprocess import check_output
from subprocess import Popen
from subprocess import PIPE

path = '.'
action = 'compile'


def file_exists(file_path):
    return os.path.isfile(file_path) if file_path \
        else False


def main(action):
    for root, dirs, files in os.walk(path):
        print('compile_all: checking ' + root)
        makefile = os.path.join(root, "Makefile")

        if file_exists(makefile):
            cmd = ['make', action]
            print("compile_all: " + ' '.join(cmd))

            if action == 'run':
                t_lang = os.getenv('TLANG')  # language name
                results_filepath = f"/opt/results/{t_lang}.txt"

                # clean measures before running
                if os.path.exists(results_filepath):
                    os.remove(results_filepath)

            if action == 'measure':
                t_lang = os.getenv('TLANG')  # language name
                measures_filepath = f"/opt/measures/{t_lang}.txt"

                # clean measures before running
                if os.path.exists(measures_filepath):
                    os.remove(measures_filepath)

            pipes = Popen(cmd, cwd=root, bufsize=0, stdout=PIPE, stderr=PIPE)
            std_out, std_err = pipes.communicate()
            std_out, std_err = std_out.decode(), std_err.decode()

            if action in ('compile', 'run'):
                if pipes.returncode and len(std_err):
                    print('[OK]')
                elif len(std_err):
                    # return code is 0 (no error), but we may want to
                    # do something with the info on std_err
                    # i.e. logger.warning(std_err)
                    print('[OK]')
                else:
                    # an error happened!
                    err_msg = "%s. Code: %s" % (std_err.strip(), pipes.returncode)
                    print('[E] Error on ' + root + ': ')
                    print(err_msg)

        if action == 'measure':
            time.sleep(5)


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=('compile', 'run', 'clean', 'measure'))
    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()
    main(namespace.action)
