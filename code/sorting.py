import random
from custom_profiler.custom_profiler import custom_line_profiler


class Sorting(object):

    def __init__(self):
        self.source_list = []
        super().__init__()

    def generate_random_list(self, start=0, end=100000, num=10000, print_result=False):
        self.source_list = random.sample(range(start, end), num)
        if print_result:
            print(self.source_list)
            print(sorted(self.source_list))

    @custom_line_profiler
    def insert_sort(self):
        for i in range(1, len(self.source_list)):
            tmp = self.source_list[i]
            for j in range(0, i):
                if tmp < self.source_list[j]:
                    self.source_list = self.source_list[:j] + [tmp] + self.source_list[j:i] + self.source_list[(i + 1):]
                    break

    def shell_sort(self):
        increment = len(self.source_list) // 2
        for i in range(len(self.source_list)):
            tmp = i
            while tmp < len(self.source_list):
                tmp += increment
                for j in range(i, tmp, increment):
                    if tmp < self.source_list[j]:
                        self.source_list = self.source_list[:j] + [tmp] + self.source_list[j:i] + self.source_list[(i + 1):]
                        break


if __name__ == '__main__':
    sorting = Sorting()
    sorting.generate_random_list(num=500)
     #sorting.insert_sort()
    sorting.shell_sort()
    # print(sorting.source_list)
