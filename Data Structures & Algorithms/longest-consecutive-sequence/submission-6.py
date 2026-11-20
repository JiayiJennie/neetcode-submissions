class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        begins = []
        s = set(nums)
        for n in s:
            if n-1 not in s:
                begins.append(n)
        best = 0
        for b in begins:
            count = 1
            x = b
            while x + 1 in s:
                count +=1 
                x += 1
            if count > best:
                best = count
        return best
            
            

            

            
        
        