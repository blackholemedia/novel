

class Recursive(object):

    def searchInsert(self, nums: list, target: int) -> int:
        if not nums:
            return 0
        length = len(nums)
        if length == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        half_length = length // 2
        if target >= nums[half_length]:
            return half_length + self.searchInsert(nums[half_length:], target)
        else:
            return self.searchInsert(nums[:half_length], target)


if __name__ == '__main__':
    a = [1, 3, 5, 6]
    b = 0
    rec = Recursive()
    print(rec.searchInsert(a, b))
