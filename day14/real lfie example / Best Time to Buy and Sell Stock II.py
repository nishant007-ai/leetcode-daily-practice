class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


#testign 
# Input: [7, 1, 5, 3, 6, 4]
# Buy at 1 → Sell at 5 (Profit = 4)
# Buy at 3 → Sell at 6 (Profit = 3)
# Total Profit = 7
Output: 7

