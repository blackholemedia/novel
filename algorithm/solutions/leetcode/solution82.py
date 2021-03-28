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
            l1 = [1, 2, 3, 3, 4, 4, 5]

            start = time.time()
            a = s.deleteDuplicates(s.pre_handle(l1))
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

    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or not head.post:
            return head
        r_head = None
        while head and head.post is not None:
            if head.val != head.post.val:
                if not locals().get('result'):
                    result = r_head = ListNode(head.val)
                else:
                    result.post = ListNode(head.val)
                    result = result.post
                head = head.post
            else:
                while head is not None:
                    if head.val == head.post.val:
                        head = head.post
                        if head.post is None:
                            head = head.post
                    else:
                        head = head.post
                        break

        if head:
            if locals().get('result'):
                result.post = ListNode(head.val)
            else:
                return head
        return r_head


if __name__ == "__main__":
    sys.exit(main())
