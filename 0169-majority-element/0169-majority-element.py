class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dist = {}
        for n in nums:
            if n not in dist:
                dist[n] = nums.count(n)

        num = nums[0]
        for k in dist:
            if dist[k] > dist[num]:
                num = k
        return num