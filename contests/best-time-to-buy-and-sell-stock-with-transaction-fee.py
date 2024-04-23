class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy = -prices[0]
        sell = 0

        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i])

            sell = max(sell, buy + prices[i] - fee)


        return sell