class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int) # val : count
        for n in nums:
            seen[n] = 1 + seen[n]

        buckets = [[] for _ in range(len(nums) + 1)] # len(nums), len(nums)-1, ..., 2, 1
        for n,c in seen.items():
            buckets[len(nums)-c].append(n)
        
        out = []
        i = 0
        for b in buckets:
            if b!= []:
                out = out + b
                i = len(out) 
                if i >= k:
                    return out[:k+1]


            




        

            
                
        