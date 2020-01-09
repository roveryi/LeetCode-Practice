'''
309. Best Time to Buy and Sell Stock with Cooldown

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''
# from discussion

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        free = 0
        have = cool = float('-inf')
        for p in prices:
            free, have, cool = max(free, cool), max(have, free - p), have + p
        return max(free, cool)

# from discussion
# https://assets.leetcode.com/users/npvinhphat/image_1560663201.png
# s0 to s1 is either buying a stock or don't do anything
# s1 to s2 is selling a stock 
# s2 to s0 is not doing anything
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        s0, s1, s2 = [], [], []
        n = len(prices)
        if n == 0 or n == 1: return 0
        
        s0.append(0)
        s1.append(-prices[0])
        s2.append(float('-inf'))
        

        
        for i in range(1,n):
            s0.append(max(s2[i-1], s0[i-1]))
            s1.append(max(s0[i-1]-prices[i], s1[i-1]))
            s2.append(prices[i] + s1[i-1])
            
        return max(s0[n-1], s2[n-1])