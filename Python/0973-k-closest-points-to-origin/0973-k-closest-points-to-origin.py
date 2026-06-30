class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        # attempt 2
        # heap
        return heapq.nsmallest(k, points, key=lambda x: ((x[0])**2 + (x[1])**2)**.5)
        
        # attempt 1
        # brute force, not efficient to pass the test cases

        # n = len(points)
        # result = []

        # for i in range(k):
        #     r = float('inf')
        #     curr = []
        #     for j in range(n):
        #         if points[j] not in result:
        #             dis = ((points[j][0])**2 + (points[j][1])**2)**.5
        #             if dis < r:
        #                 r = min(dis, r)
        #                 curr = points[j]
            
        #     result.append(curr)
        # return result

            
