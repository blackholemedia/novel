"""
Module docstring.
"""

import sys
import getopt

from algorithm.solutions.stack import Stack


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
            string = '([)]'
            print(s.isValid(string))

        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


class Solution:

    def isValid(self, s: str) -> bool:
        my_stack = Stack()
        for i in s:
            if my_stack.is_empty():
                my_stack.push(i)
            else:
                if self.match(my_stack.top(), i):
                    my_stack.pop()
                else:
                    my_stack.push(i)
        if my_stack.is_empty():
            return True
        else:
            return False

    def __init__(self):
        self._mapping = {
            '{': '}',
            '(': ')',
            '[': ']',
        }

    def match(self, a, b):
        if b == self._mapping.get(a):
            return True
        else:
            return False


if __name__ == "__main__":
    sys.exit(main())
