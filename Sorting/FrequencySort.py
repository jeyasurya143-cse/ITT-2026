class Solution(object):
    def frequencySort(self, s):
        freq = dict()
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = ""
        for key, value in sorted_freq:
            ans += key * value
        return ans
