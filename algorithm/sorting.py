from custom_profiler.custom_profiler import custom_line_profiler
from algorithm.base import SortingBase


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

    def merge_sort(self):
        return self._merge_sort(self.source_list)

    def _merge_sort(self, array):
        length = len(array)
        if length < 2:
            return array
        elif length == 2:
            return [min(array), max(array)]
        else:
            left = self._merge_sort(array[:(len(array) // 2)])
            right = self._merge_sort(array[(len(array) // 2):])
            i, j, result = 0, 0, []
            while True:
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                    if i >= len(left):
                        result.extend(right[j:])
                        break
                else:
                    result.append(right[j])
                    j += 1
                    if j >= len(right):
                        result.extend(left[i:])
                        break
            return result


if __name__ == '__main__':
    sorting = Sorting()
    sorting.generate_random_list(start=0, end=1000, num=100, print_result=True)
    # sorting.insert_sort()
    # sorting.shell_sort()
    print(sorting.merge_sort())
    pass
    #print(sorting.source_list)
