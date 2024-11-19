class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # empty
        if not intervals:
            return []
        
        # sort intervals by start time
        intervals.sort(key = lambda x: x[0])
        result = [intervals[0]]
        n = len(intervals)
        for i in range(1, n):
            last_added = result[-1]
            # current interval overlaps w/ last added interval
            # [1, 3]; end time = 3
            # [2, 6]; end time = 2
            # 3 > 2
            if last_added[1] >= intervals[i][0]:
                # merge
                last_added[1] = max(last_added[1], intervals[i][1])
            else:
                # add current interval to result
                result.append(intervals[i])
        return result