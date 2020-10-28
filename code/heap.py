"""
Module docstring.
"""

import sys
import getopt


class Heap(object):

    def __init__(self, array: list):
        length = len(array)
        start = length // 2
        while start > 1:
            for i in range(start, end):
                if (2 * i + 1) > length:
                    continue
                pass
            self.heap = ''

    def up_node(self):
        pass

    def down_node(self):
        pass


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
