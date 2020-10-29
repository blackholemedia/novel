"""
Module docstring.
"""

import sys
import getopt

from .sorting import SortingBase


class Heap(SortingBase):

    def __init__(self, array: list):
        if array is not None:
            self.source_list = array
        super().__init__()
        self.build_heap()
#        length = len(array)
#        i = length // 2 - 1
#        while i >= 0:
#            if (2 * i + 1) >= length:
#                continue
#            if (2 * i + 2) >= length:
#                if array[i] > array[2 * i + 1]:
#                    array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
#            else:
#                if array[i] > min(array[1], array[2]):
#                    if array[2 * i + 1] <= array[2 * i + 1]:
#                        array[i], array[2 * i + 1] = array[2 * i + 1], array[i]
#                    else:
#                        array[i], array[2 * i + 2] = array[2 * i + 2], array[i]

    def build_heap(self):
        length = len(self.source_list)
        i = length // 2 - 1
        while i >= 0:
            if (2 * i + 1) >= length:
                continue
            if (2 * i + 2) >= length:
                if self.source_list[i] > self.source_list[2 * i + 1]:
                    self.source_list[i], self.source_list[2 * i + 1] = self.source_list[2 * i + 1], self.source_list[i]
            else:
                if self.source_list[i] > min(self.source_list[1], self.source_list[2]):
                    if self.source_list[2 * i + 1] <= self.source_list[2 * i + 1]:
                        self.source_list[i], self.source_list[2 * i + 1] = self.source_list[2 * i + 1], self.source_list[i]
                    else:
                        self.source_list[i], self.source_list[2 * i + 2] = self.source_list[2 * i + 2], self.source_list[i]

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
