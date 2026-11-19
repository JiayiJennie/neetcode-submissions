class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {} # val : indx
        for i,x in enumerate(nums):
            if x in prevMap:
                return True
            else:
                prevMap[x] = i
        return False
        