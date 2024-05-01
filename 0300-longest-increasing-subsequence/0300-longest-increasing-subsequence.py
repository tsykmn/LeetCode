class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1]*n
        size = 0

        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i+j)/2
                if dp[m] < x:
                    i = m+1
                else:
                    j=m
            dp[i] = x
            if i == size:
                size += 1
        return size