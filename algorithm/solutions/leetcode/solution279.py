"""
Module docstring.
"""

import sys
import getopt
import time

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
            n = 34
            start = time.time()
            print(s.numSquares(n))
            print(time.time() - start)

        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [9999999999] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        squares = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        for i in range(2, n + 1):
            for square in squares:
                if square > i:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        return dp[-1]


if __name__ == "__main__":
    sys.exit(main())
