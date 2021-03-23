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
            string = ["4","13","5","/","+"]
            print(s.evalRPN(string))

        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


class Solution:
    def evalRPN(self, tokens: list) -> int:
        a = Stack()
        for i in tokens:
            if a.is_empty():
                a.push(i)
                continue
            if i not in ['+', '-', '*', '/']:
                a.push(i)
            else:
                b = a.pop()
                c = a.pop()
                a.push(str(int(eval(c+i+b))))
        return int(a.pop())


if __name__ == "__main__":
    sys.exit(main())
