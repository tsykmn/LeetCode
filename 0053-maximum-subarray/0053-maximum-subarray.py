class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currResult = nums[0]
        maxResult = nums[0]
        n = len(nums)

        for i in range(1, n):
            currResult = max(nums[i], currResult+nums[i])
            maxResult = max(currResult, maxResult)

        return maxResult