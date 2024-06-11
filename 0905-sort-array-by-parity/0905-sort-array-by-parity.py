class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd