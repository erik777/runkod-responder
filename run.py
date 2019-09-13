import argparse
import os
import sys
import logging

logging.basicConfig(level=logging.INFO)

assert sys.version_info[0] == 3 and sys.version_info[1] >= 7, 'Requires Python 3.7 or newer'

os.sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from responder.util import assert_env_vars

assert_env_vars('MONGO_URI')


def main():
    parser = argparse.ArgumentParser(description='')
    cmd_list = (
        'web',
        'test'
    )

    parser.add_argument('cmd', choices=cmd_list, nargs='?', default='app')

    args = parser.parse_args()
    cmd = args.cmd

    if cmd == 'web':
        from responder.web.app import main
        main()

    if cmd == 'test':
        from responder.test import do_tests
        do_tests()


if __name__ == '__main__':
    main()
