class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        copy_set = set(nums)
        result = list()

        for i in range(1, n + 1):
            if i not in copy_set:
                result.append(i)

        return result
