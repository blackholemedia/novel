"""
Module docstring.
"""

import sys
import getopt
import time

from algorithm.solutions.stack import ListNode


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
            s = Solution()
            # l1 = [1, 1, 2]
            # l1 = [1, 1, 1]
            # l1 = [1, 1, 2, 3, 3]
            l1 = []

            start = time.time()
            a = s.reverseList(s.pre_handle(l1))
            while a:
                print(a.val)
                a = a.post
            end = time.time()
            print(end - start)

        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


class Solution:

    def pre_handle(self, l1):
        if not l1:
            l3 = None
        for i in l1[::-1]:
            if not locals().get('l3'):
                l3 = ListNode(val=i)
            else:
                l3 = ListNode(val=i, post=l3)
        return l3

    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            if pre:
                post = head.post
                head.post = pre
                pre = head
                head = post
            else:
                pre = ListNode(head.val)
                head = head.post
        return pre


if __name__ == "__main__":
    sys.exit(main())
