class Solution(object):
    def removeKdigits(self, num, k):
        if len(num) == k:
            return "0"
            
        stack = list()
        stack.append(num[0])
        i = 1
        while i < len(num): 
            while stack and k > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
            i += 1
        
        while k > 0 and stack:
            stack.pop()
            k -= 1

        result = "".join(stack).lstrip('0')
        return result if result else "0"
