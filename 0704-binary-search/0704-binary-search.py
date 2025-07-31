class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        s = 0
        e = len(nums)-1
        while s <= e:
            mid = (e - s)//2 + s

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                e = mid-1
            elif nums[mid] < target:
                s = mid+1
        return -1