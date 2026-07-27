class Solution(object):
    def findErrorNums(self, nums):
        curr = dict()
        n = len(nums)
        res = [0, 0]

        for i in range(n):
            if nums[i] not in curr:
                curr[nums[i]] = 1
            else:
                curr[nums[i]] += 1

        for i in range(1, n + 1):
            if curr.get(i, 0) == 2:
                res[0] = i
            elif i not in curr:
                res[1] = i

        return res
