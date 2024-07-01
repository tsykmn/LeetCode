class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # stones.sort()
        # while stones:
        #     s1 = stones.pop()
        #     if not stones:
        #         return s1
        #     s2 = stones.pop()
        #     if s1 > s2:
        #         n = len(stones)
        #         for i in range(n+1):
        #             if i == n or stones[i] >= s1-s2:
        #                 stones.insert(i, s1-s2)
        #                 break
        # return 0
        # my solution
        # make a helper function
        def helper(stone):
        # if there is only 1 stone or none remaining
            if 1 == len(stone):
                return stone[0]
            elif len(stone) == 0:
                return 0
            n = len(stone)
            n1 = max(stone) # get the 1st biggest number
            stone.remove(n1)
            n2 = max(stone) # get the 2nd biggest number
            stone.remove(n2)
            if n1 != n2: # add if not same
                stone.append(abs(n1-n2))
            return helper(stone)
        return helper(stones)
        