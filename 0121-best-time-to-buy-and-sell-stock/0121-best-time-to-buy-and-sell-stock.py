class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        n = len(prices)
        profit = 0
        for i in range(n):
            p = max(prices[i:]) - prices[i]
            if p >= 0 and profit < p:
                profit = p
        return profit
        # least = min(prices)
        # index = 0
        # n = len(prices)
        # for i in range(n):
        #     if prices[i] == least:
        #         index = i
        # if index == (n - 1):
        #     return 0
        # else:
        #     profit = 0
        #     for j in range(index, n):
        #         if profit < (prices[j] - least):
        #             profit = prices[j] - least
        #     return profit
        