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
            l1 = [2, 1]
            # l1 = [1, 1, 1]
            # l1 = [1, 1, 2, 3, 3]
            # l1 = [1,4,3,2,5,2]
            x = 2

            start = time.time()
            a = s.partition(s.pre_handle(l1), x)
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

    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        r1_head, r2_head = None, None
        while head:
            if head.val < x:
                if not locals().get('r1'):
                    r1_head = r1 = ListNode(head.val)
                else:
                    r1.post = ListNode(head.val)
                    r1 = r1.post
            else:
                if not locals().get('r2'):
                    r2_head = r2 = ListNode(head.val)
                else:
                    r2.post = ListNode(head.val)
                    r2 = r2.post
            head = head.post
        if r1_head:
            r1.post = r2_head
        else:
            return r2_head

        return r1_head


if __name__ == "__main__":
    sys.exit(main())
