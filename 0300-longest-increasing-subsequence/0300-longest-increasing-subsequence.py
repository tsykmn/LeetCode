class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Initialize dp with a matrix
        n = len(nums)
        dp = [1]*n
        size = 0

        # Iterate from the last element of the sequence
        for i in range(n - 1, -1, -1):
            # Iterate elements after i
            # check if the elements after i is larger than i or not
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

        # Alternate Solution
        # n = len(nums)
        # dp = [1]*n
        # size = 0

        # for x in nums:
        #     i, j = 0, size
        #     while i != j:
        #         m = (i+j)/2
        #         if dp[m] < x:
        #             i = m+1
        #         else:
        #             j=m
        #     dp[i] = x
        #     if i == size:
        #         size += 1
        # return size