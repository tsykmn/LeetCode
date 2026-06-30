class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        p, profit = prices[0], 0
        
        for i in range(n):
            if p > prices[i]:
                p=prices[i]
            profit = max(profit, prices[i]-p)
        return profit