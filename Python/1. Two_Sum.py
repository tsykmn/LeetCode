def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            current = nums[i] + nums[j]
            if target == current:
                return [i, j]
    return []
