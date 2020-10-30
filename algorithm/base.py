"""
Module docstring.
"""

import sys
import getopt
import random


class SortingBase(object):

    def __init__(self):
        self.source_list = []
        super().__init__()

    def generate_random_list(self, start=0, end=100000, num=10000, print_result=False):
        self.source_list = random.sample(range(start, end), num)
        if print_result:
            print(self.source_list)
            print(sorted(self.source_list))


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "ho:", ["help", "output="])  # short: h means switch, o means argument
            # required; long: help means switch, output means argument required
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


if __name__ == "__main__":
    sys.exit(main())
