class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if stones == [1]:
            return 1
        def helper(stone):
            if 1 == len(stone):
                return stone[0]
            elif len(stone) == 0:
                return 0
            n = len(stone)
            n1 = max(stone)
            stone.remove(n1)
            n2 = max(stone)
            stone.remove(n2)
            if n1 != n2:
                stone.append(abs(n1-n2))
            return helper(stone)
        return helper(stones)
        