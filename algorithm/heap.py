"""
Module docstring.
"""

import sys
import getopt

from algorithm.sorting import SortingBase


class Heap(SortingBase):

    def __init__(self, array=None, **kwargs):
        super().__init__()
        if array is not None:
            self.source_list = array
        else:
            self.generate_random_list(**kwargs)
        self.build_heap()

    def build_heap(self):
        length = len(self.source_list)
        i = length // 2 - 1
        while i >= 0:
            self.down_node(i, length)
            i -= 1

    def up_node(self):
        pass

    def down_node(self, p, length):
        while True:
            left, right = 2 * p + 1, 2 * p + 2
            if left >= length:
                break
            if right >= length:
                if self.source_list[p] > self.source_list[left]:
                    self.source_list[p], self.source_list[left] = self.source_list[left], self.source_list[p]
                    p = left
                else:
                    break
            else:
                if self.source_list[p] > min(self.source_list[left], self.source_list[right]):
                    if self.source_list[left] <= self.source_list[right]:
                        self.source_list[p], self.source_list[left] = self.source_list[left], self.source_list[p]
                        p = left
                    else:
                        self.source_list[p], self.source_list[right] = self.source_list[right], self.source_list[p]
                        p = right
                else:
                    break


class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg


def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hs:e:n:p:", ["help", "start=", "end=", "num=", "print_result="])  # short: h means switch, o means argument
            # required; long: help means switch, output means argument required
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
        params = {k[0].lstrip('--'): int(k[1]) for k in opts}
        heap = Heap(array=[7, 14, 17, 12, 13, 15, 11, 5, 3, 10], **params)
        print(heap.source_list)
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


if __name__ == "__main__":
    sys.exit(main())
