class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # get the two heaviest stones and smash them together
        # 2 conditionals
        # if x == y, remove them from stones
        # if x != y, remove x and change y to y - x

        def helper(stone):
            n = len(stone)

            # if one stone remains
            if n == 1:
                return stone[0]
            # no stone remaining
            elif n < 1:
                return 0

            # get two heaviest stones
            s1 = max(stone)
            stone.remove(s1)
            s2 = max(stone)
            stone.remove(s2)

            if s1 != s2:
                stone.append(abs(s1 - s2))
            return helper(stone)

        return helper(stones)