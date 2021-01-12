"""
Module docstring.
"""

import sys
import getopt

import numpy as np
import matplotlib.pyplot as plt


class Demo(object):

    @staticmethod
    def f(t):
        return np.exp(-t) * np.cos(2 * np.pi * t)

    def display(self):
        t1 = np.arange(0.0, 5.0, 0.1)
        t2 = np.arange(0.0, 5.0, 0.02)

        plt.figure(dpi=100)
        plt.subplot(211)
        plt.plot(t1, self.f(t1), color='tab:blue', marker='o')
        plt.plot(t2, self.f(t2), color='black')
        plt.title('demo')

        plt.subplot(212)
        plt.plot(t2, np.cos(2 * np.pi * t2), color='tab:orange', linestyle='--')
        plt.suptitle('matplotlib.pyplot api')
        plt.show()


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
            d = Demo()
            d.display()
        except getopt.error as msg:
            raise Usage(msg)
        # more code, unchanged
    except Usage as err:
        print(sys.stderr, err.msg)
        print(sys.stderr, "for help use --help")
        return 2


if __name__ == "__main__":
    sys.exit(main())
