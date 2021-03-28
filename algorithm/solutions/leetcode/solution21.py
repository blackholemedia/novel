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
            l1 = []
            l2 = [0]
            start = time.time()
            a = s.mergeTwoLists(*s.pre_handle(l1, l2))
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

    def pre_handle(self, l1, l2):
        if not l1:
            l3 = None
        for i in l1[::-1]:
            if not locals().get('l3'):
                l3 = ListNode(val=i)
            else:
                l3 = ListNode(val=i, post=l3)
        if not l2:
            l4 = None
        for i in l2[::-1]:
            if not locals().get('l4'):
                l4 = ListNode(val=i)
            else:
                l4 = ListNode(val=i, post=l4)
        return l3, l4

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            p = l1
            o = l2
        else:
            p = l2
            o = l1
        result = head = ListNode(p.val)
        while p.post is not None:
            if p.post.val <= o.val:
                p = p.post
            else:
                p, o = o, p.post
            result.post = p
            result = result.post
        if o is not None:
            result.post = o
        return head


if __name__ == "__main__":
    sys.exit(main())
