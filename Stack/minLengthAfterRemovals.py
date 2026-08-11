class Solution(object):
    def minLengthAfterRemovals(self, s):
        stack = list()
        
        for i in range(0, len(s)):
            if stack and stack[-1] != s[i]:
                stack.pop()
            else:
                stack.append(s[i])
                
        return len(stack)
