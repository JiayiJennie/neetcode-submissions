class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # val : count
        maxFreq = 0
        maxLen = 0
        
        i = 0
        for j in range(len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            maxFreq = max(maxFreq, count[s[j]])
            while maxFreq + k < j - i + 1:
                count[s[i]] -= 1
                i += 1
            maxLen = max(maxLen, j - i + 1)
        return maxLen


            


        