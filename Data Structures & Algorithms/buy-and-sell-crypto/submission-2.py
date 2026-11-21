class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minb = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minb)
            minb = min(minb, sell)
        return maxP

        