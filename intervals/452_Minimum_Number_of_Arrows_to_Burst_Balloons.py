from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        res = len(points)

        for i, point in enumerate(points[1:]):
            if points[i][1]>=point[0]:
                res-=1
            else:
                pass

        return res

print(Solution().findMinArrowShots(points = [[10,16],[2,8],[1,6],[7,12]]))

# 123456789123456
# [    ]
#  [     ]
#       [   ]
#          [    ]
