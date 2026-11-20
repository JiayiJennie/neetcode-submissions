class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd = []
        surfixProd = []

        for i in range(len(nums)-1):
            if i == 0:
                prefixProd.append(nums[i])
                surfixProd.append(nums[-1])
            else:
                n = nums[i]
                m = nums[len(nums)-i-1]
                nextPrefix = n * prefixProd[-1]
                nextSurfix = m * surfixProd[-1]
                prefixProd.append(nextPrefix)
                surfixProd.append(nextSurfix)

        prefixProd = [1] + prefixProd
        surfixProd = surfixProd[::-1] + [1]

        res = []
        for j in range(len(nums)):
            res.append(prefixProd[j]*surfixProd[j])
        return res


        