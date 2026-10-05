class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                max_profit += prices[i+1] - prices[i]

        return max_profit
