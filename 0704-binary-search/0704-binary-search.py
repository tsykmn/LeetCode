class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            n = len(nums)
            for i in range(n):
                if target == nums[i]:
                    return i
        return -1
