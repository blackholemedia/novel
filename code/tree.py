from custom_profiler.custom_profiler import custom_line_profiler


class Tree(object):

    @custom_line_profiler
    def get(self):
        pass


if __name__ == '__main__':
    rec = Tree()
