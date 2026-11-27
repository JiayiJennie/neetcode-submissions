class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        count = [0]*95
        maxLen = 0

        i = 0
        for j in range(len(s)):
            idxj = ord(s[j]) - ord(" ")
            if count[idxj] == 1:
                while s[i] != s[j]:
                    idxi = ord(s[i]) - ord(" ")
                    count[idxi] -= 1
                    i += 1
                i += 1
            else:
                count[idxj] += 1
                maxLen = max(j-i+1, maxLen)

        return maxLen
