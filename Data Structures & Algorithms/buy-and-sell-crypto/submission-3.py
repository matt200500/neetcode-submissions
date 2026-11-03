class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value = 101
        profit = 0
        for index in range(len(prices)):
            min_value = min(min_value,prices[index])
            if min_value < prices[index]:
                current_profit = prices[index] - min_value
                profit = max(profit,current_profit)
        return profit




        