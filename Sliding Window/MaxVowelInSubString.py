class Solution(object):
    def maxVowels(self, s, k):
        vowel = "aeiou"
        current_count = 0
        
        for i in range(k):
            if s[i] in vowel:
                current_count += 1
        
        max_count = current_count
        
        for i in range(k, len(s)):
            if s[i] in vowel:
                current_count += 1
                
            if s[i - k] in vowel:
                current_count -= 1
                
            if current_count > max_count:
                max_count = current_count

        return max_count
