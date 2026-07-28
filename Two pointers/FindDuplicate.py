class Solution(object):
    def findDuplicate(self, nums):
        nums.sort()
        slow=nums[0]
        for i in range(1,len(nums)):
            if slow == nums[i]:
                return nums[i]
            else:
                slow=nums[i]
