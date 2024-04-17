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
    # def count(goal, arr):
    #     current = 0
    #     indices = []
    #     for i in range(len(arr)):
    #         goal -= arr[i]
    #         indices.append(i)
    #         if goal == 0:
    #             return [0, indices]
    #         elif goal < 0:
    #             return [1]

    # n = len(nums)
    # for i in range(n):
    #     counted = count(target, nums[i:])
    #     if counted[0] == 0:
    #         return counted[1]
    # return []
