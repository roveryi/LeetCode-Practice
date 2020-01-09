'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
# find the max profit the first, then find the max profit of the second
# O(N^2)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def maxOne(p):
            current_min = float('inf')
            ans = 0
            n = len(p)
            if n == 0: return 0
            
            for i in range(n):
                current_min  = min(current_min, p[i])
                ans = max(ans, p[i]-current_min)
                
            return ans
        
        n = len(prices)  
        if n == 0: return 0
        
        profits = []
        
        for i in range(n):
            profits.append(maxOne(prices[0:i])+maxOne(prices[i:]))
        
        return max(profits)

# From discussion
# Forward and backward traversal, dynamic programming     
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = float('inf')
        current_max = float('-inf')
        profit = []
        n = len(prices)
        total_max, max_profit = 0, 0
        if n == 0: return 0
        
        for i in range(n):
            current_min = min(prices[i], current_min)
            max_profit = max(max_profit, prices[i] - current_min)
            profit.append(max_profit)
        max_profit = 0    
        for i in range(n-1,-1,-1):
            current_max = max(prices[i], current_max)
            max_profit = max(max_profit, current_max - prices[i])
            total_max = max(total_max, max_profit + profit[i])
            
        return total_max        