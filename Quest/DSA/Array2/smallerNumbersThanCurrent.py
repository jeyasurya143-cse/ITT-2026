class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        result=list()
        for i in range(0,len(nums)):
            count=0
            for j in range (len(nums)):
                if nums[j] < nums[i] :
                    count+=1
            result.append(count)
        return result
