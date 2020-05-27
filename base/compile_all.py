import os
import time
import argparse

from subprocess import check_output  # nosec
from subprocess import CalledProcessError  # nosec
from subprocess import PIPE  # nosec

path = '.'
action = 'compile'


def file_exists(fpath: str) -> bool:
    return os.path.isfile(fpath) if fpath \
        else False


def clean_results():
    t_lang = os.getenv('TLANG')  # language name
    results_filepath = f"/opt/results/{t_lang}.txt"

    # clean measures before running
    if os.path.exists(results_filepath):
        os.remove(results_filepath)


def clean_measures(lang):
    t_lang = os.getenv('TLANG')  # language name
    measures_filepath = f"/opt/measures/{t_lang}.txt"

    # clean measures before running
    if os.path.exists(measures_filepath):
        os.remove(measures_filepath)


def main(actions: str, only: str = ''):
    for action in actions:
        print(f"> ACTION: {action}")

        for root, dirs, files in os.walk(path):
            if only not in root:
                print(f"compile_all: skipping {root}")
                continue

            print(f"compile_all: checking {root}")

            test_name = os.path.basename(root)
            makefile = os.path.join(root, "Makefile")

            if file_exists(makefile):
                cmd = ['make', f'TEST_NAME={test_name}', action]
                print(("compile_all: " + ' '.join(cmd)).strip())

                if action == 'run':
                    clean_results()

                if action == 'measure':
                    clean_measures()

                try:
                    msg = check_output(
                        cmd,
                        cwd=root,
                        stderr=PIPE
                    ).decode('utf-8').strip()

                    if action in ('compile', 'run'):
                        print(f"[OK] {msg}")
                except CalledProcessError as err:
                    out_msg = err.stdout.decode().strip()
                    err_msg = err.stderr.decode().strip()
                    err_code = err.returncode

                    print(f"[M] {out_msg}; Code {err_code}")
                    print(f"[E] {err_msg}; Code {err_code}")
            else:
                print(f"compile_all: ignoring {root}")

            if action == 'measure':
                time.sleep(5)


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('actions', choices=(
        'prepare', 'compile', 'run', 'clean', 'measure'
    ), nargs='+')
    parser.add_argument(
        '-o', '--only', type=str, default='',
        help='only run requested test'
    )
    return parser


if __name__ == '__main__':
    parser = make_parser()
    namespace, args = parser.parse_known_args()
    main(namespace.actions, namespace.only)
