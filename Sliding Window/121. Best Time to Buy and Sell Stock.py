# Time complexity: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 9999
        res = 0
        for i in range(0, len(prices)):
            if prices[i] < min_buy:
                min_buy = prices[i]
            elif prices[i] - min_buy > res:
                res = prices[i] - min_buy
        return res

        