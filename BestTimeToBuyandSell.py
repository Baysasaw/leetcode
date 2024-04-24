# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# https://leetcode.com/submissions/detail/289272619/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         low_buy = prices[0]
#         Max_profit = 0

#         for i in range(1, len(prices)):
#             if low_buy > prices[i]:
#                 low_buy = prices[i]
#             else:
#                 profit = prices[i] - low_buy
#                 Max_profit = max(Max_profit,profit)
#         return Max_profit


# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# https://leetcode.com/submissions/detail/289273529/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit
