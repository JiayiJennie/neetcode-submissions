class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        buckets = [[] for _ in range(len(nums) + 1)] # len(nums), len(nums)-1, ..., 2, 1

        for n in nums:
            seen[n] = 1 + seen.get(n,0)

        for n,c in seen.items():
            buckets[len(nums)-c].append(n)
        
        res = []
        for b in buckets:
            if b!= []:
                res = res + b
                if len(res) >= k:
                    return res[:k+1]


            




        

            
                
        