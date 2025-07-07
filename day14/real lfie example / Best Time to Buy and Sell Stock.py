class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


#testing 
#Input: [7, 1, 5, 3, 6, 4]
# Buy at 1 (day 1), sell at 6 (day 4) → Profit = 5
Output: 5
