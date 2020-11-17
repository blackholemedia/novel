from custom_profiler.custom_profiler import custom_line_profiler
from algorithm.base import SortingBase
from algorithm.base_structure.heap import Heap


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

    def bucket_sort(self, bucket_size=10):
        min_value, max_value = min(self.source_list), max(self.source_list)
        buckets = [[] for i in range(max_value // bucket_size - min_value // bucket_size + 1)]
        for i in self.source_list:
            buckets[(i - min_value) // bucket_size].append(i)
        self.source_list.clear()
        for i in buckets:
            heap = Heap(array=i)
            heap.heap_sort()
            self.source_list.extend(heap.source_list)

    def bubble_sort(self):
        length = len(self.source_list)
        for i in range(length - 1):
            j = 1
            while j < length - i:
                if self.source_list[j] < self.source_list[j - 1]:
                    self.source_list[j], self.source_list[j - 1] = self.source_list[j - 1], self.source_list[j]
                j += 1

    def quick_sort(self):
        self.source_list = self._quick_sort(self.source_list)

    def _quick_sort(self, array):
        length = len(array)
        if not length or length == 1:
            return array
        if length == 2:
            if array[0] > array[1]:
                array[0], array[1] = array[1], array[0]
            return array
        else:
            middle = length // 2
            # get middle value as pivot
            if array[0] >= array[middle]:
                if array[middle] >= array[-1]:
                    pivot = middle
                elif array[0] >= array[-1]:
                    pivot = -1
                else:
                    pivot = 0
            else:
                if array[middle] <= array[-1]:
                    pivot = middle
                elif array[0] >= array[-1]:
                    pivot = 0
                else:
                    pivot = -1
            # dividend
            if pivot == middle:
                array[-1], array[middle] = array[middle], array[-1]
                pivot = -1
            if pivot == 0:
                i, j = 1, length - 1
            else:
                i, j = 0, length - 2
            while i < j:
                if array[i] > array[pivot] > array[j]:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                    j -= 1
                    continue
                if array[i] >= array[pivot]:
                    j -= 1
                    continue
                if array[pivot] >= array[j]:
                    i += 1
                    continue
                i += 1
                j -= 1
            # exchange pivot
            if pivot == -1:
                if array[pivot] <= array[i]:
                    array[pivot], array[i] = array[i], array[pivot]
                    pivot = i
                else:
                    array[pivot], array[i + 1] = array[i + 1], array[pivot]
                    pivot = i + 1
            else:
                if array[pivot] <= array[i]:
                    array[pivot], array[i - 1] = array[i - 1], array[pivot]
                    pivot = i - 1
                else:
                    array[pivot], array[i] = array[i], array[pivot]
                    pivot = i
            # conquer
            array = self._quick_sort(array[:pivot]) + [array[pivot]] + self._quick_sort(array[(pivot + 1):])
            return array


if __name__ == '__main__':
    sorting = Sorting()
    sorting.generate_random_list(start=0, end=1000, num=10, print_result=True)
    # sorting.insert_sort()
    # sorting.shell_sort()
    # print(sorting.merge_sort())
    # sorting.bucket_sort(bucket_size=13)
    sorting.quick_sort()
    print(sorting.source_list)
    pass
