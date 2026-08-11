class Solution(object):
    def removeDuplicateLetters(self, s):
        last_occurrence = {}
        for i in range(len(s)):
            last_occurrence[s[i]] = i
            
        stack = list()
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                continue
                
            while len(stack) and s[i] < stack[-1] and last_occurrence[stack[-1]] > i:
                removed = stack.pop()
                seen.remove(removed)
                
            stack.append(s[i])
            seen.add(s[i])
            
        return ''.join(stack)
