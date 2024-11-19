class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        buy, profit = prices[0], 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if (prices[i] - buy) > profit:
                profit = prices[i] - buy

        return profit
