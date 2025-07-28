class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                total = nums[j] + nums[i]
                if total == target:
                    return [j, i]
        return 0