class Solution(object):
    def sortedSquares(self, nums):
        res=list()
        for i in range(len(nums)):
            sqr=nums[i]**2
            res.append(sqr)
        res.sort()
        return res
