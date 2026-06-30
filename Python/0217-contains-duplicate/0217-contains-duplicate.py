class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nCount = Counter(nums)

        for i in nCount.values():
            if i >= 2:
                return True
        return False