class Solution(object):
    def minAddToMakeValid(self, s):
        open_stack = list()
        close_needed = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                open_stack.append(s[i])
            else:
                if open_stack:
                    open_stack.pop()
                else:
                    close_needed += 1
                    
        return len(open_stack) + close_needed
