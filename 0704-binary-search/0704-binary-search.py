class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # alternate
        # initialize right (end) and left (start)
        # if mid == target: index of mid
        # if mid < target: left = mid + 1
        # mid > target: mid - 1
        n = len(nums)
        left = 0
        right = n - 1
        while left <= right:
            middle = left + (right-left)/2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1
        # my way
        # if target in nums:
        #     n = len(nums)
        #     for i in range(n):
        #         if target == nums[i]:
        #             return i
        # return -1
