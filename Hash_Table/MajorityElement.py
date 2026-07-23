class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        freq = len(nums) // 3
        nums.sort()
        result = set()
        count = 1
        if count > freq:
            result.add(nums[0])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1 
            if count > freq:
                result.add(nums[i]) 
        return list(result)
