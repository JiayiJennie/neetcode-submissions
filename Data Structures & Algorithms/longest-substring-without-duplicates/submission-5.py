class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        idxmap = [-1]*95 # idx of first appeat this charactor
        maxLen = 0

        i = 0
        for j in range(len(s)):
            idx = self.getIdx(s[j])
            if idxmap[idx] >= i:
                i = idxmap[idx] + 1
            idxmap[idx] = j
            maxLen = max(j-i+1, maxLen)

        return maxLen

    def getIdx(self, c):
        return ord(c) - ord(" ")
