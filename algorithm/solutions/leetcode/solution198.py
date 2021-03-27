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
            string = [2,7,9,3,1]
            start = time.time()
            print(s.rob(string))
            end = time.time()
            print(end-start)

        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


class Solution:
    def rob(self, nums: list) -> int:
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        dp = [0] * length
        dp[0] = nums[0]
        dp[1] = max(nums[:2])
        for i in range(2, length):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1]


if __name__ == "__main__":
    sys.exit(main())
