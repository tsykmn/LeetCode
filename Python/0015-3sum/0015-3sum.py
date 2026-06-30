class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            # continue moving i if duplicated to the next one
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            j = i + 1
            k = n-1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # nums is sorted
                # moving k to left helps to decrease total/sum since k is at the end and biggest number
                if total > 0:
                    k -= 1
                # moving j to right increase total
                elif total < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    # remove duplicated values while maintain the boundaries
                    while nums[j] == nums[j-1] and j < k:
                        j += 1

        return result