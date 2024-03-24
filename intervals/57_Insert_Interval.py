from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return newInterval

        intervals_min = [newInterval[0] - interval[0] for interval in intervals]
        place = len(intervals)
        for i, el in enumerate(intervals_min):
            if el<=0:
                place = i
                break
            else:
                pass

        intervals.insert(place, newInterval)

        res = [intervals[0]]

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res


print(Solution().insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))