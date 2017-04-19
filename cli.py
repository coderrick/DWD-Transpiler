#!/usr/bin/python3

import sys
import getopt

import core

def usage():
    print('\n'
          'Usage: dwd [input]\n'
          '\n'
          '    A modular transcompiler\n'
          '\n'
          'Commands:\n'
          '    foo        lorem ipsum\n'
          '\n'
          'Options:\n'
          '    -h, --help       show the help\n')


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "h", ["help"])

    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()

    try:

        if 'foo' in args:
            print('Lorem ipsum')

        else:
            print('Wrong command. See help (--help or -h).')

    except:
        pass

    return 0


if __name__ == '__main__':
    main(sys.argv[:1])
