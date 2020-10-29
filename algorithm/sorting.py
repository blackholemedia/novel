import random
from custom_profiler.custom_profiler import custom_line_profiler


class SortingBase(object):

    def __init__(self):
        self.source_list = []
        super().__init__()

    def generate_random_list(self, start=0, end=100000, num=10000, print_result=False):
        self.source_list = random.sample(range(start, end), num)
        if print_result:
            print(self.source_list)
            print(sorted(self.source_list))


class Sorting(SortingBase):

    def __init__(self):
        super().__init__()

    @custom_line_profiler
    def insert_sort(self):
        for i in range(1, len(self.source_list)):
            tmp = self.source_list[i]
            for j in range(0, i):
                if tmp < self.source_list[j]:
                    self.source_list = self.source_list[:j] + [tmp] + self.source_list[j:i] + self.source_list[(i + 1):]
                    break

    @custom_line_profiler
    def shell_sort(self):
        total_length = len(self.source_list)
        increment = total_length // 2
        while increment > 0:
            for i in range(increment):
                tmp = i
                while tmp < total_length:
                    tmp += increment
                    if tmp >= total_length:
                        break
                    catch_flag = False
                    for j in range(i, tmp + 1, increment):
                        if catch_flag:
                            self.source_list[j], previous = previous, self.source_list[j]
                            continue
                        if self.source_list[tmp] < self.source_list[j]:
                            catch_flag = True
                            previous = self.source_list[j]
                            self.source_list[j] = self.source_list[tmp]
            increment //= 2


if __name__ == '__main__':
    sorting = Sorting()
    sorting.generate_random_list(num=1000, print_result=False)
    # sorting.insert_sort()
    sorting.shell_sort()
    #print(sorting.source_list)
