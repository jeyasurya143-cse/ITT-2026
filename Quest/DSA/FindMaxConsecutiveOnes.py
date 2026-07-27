class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        one_count=0
        max_count=0
        count_list=list()
        for i in range(len(nums)):
            if nums[i]==1:
                one_count+=1
            else:
                count_list.append(one_count)
                one_count=0
        count_list.append(one_count)
        return max(count_list)
