class Solution(object):
    def canSeePersonsCount(self, heights):
        n = len(heights)
        result = [0] * n
        stack = []
        
        for i in range(n - 1, -1, -1):
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                result[i] += 1
                
            if stack:
                result[i] += 1
                
            stack.append(i)
            
        return result
