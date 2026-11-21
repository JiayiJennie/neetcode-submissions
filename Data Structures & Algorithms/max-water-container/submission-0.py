class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l,r = 0, len(heights)-1
        while l < r:
            water = (r-l) * min(heights[l],heights[r])
            if water > best:
                best = water
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best

        