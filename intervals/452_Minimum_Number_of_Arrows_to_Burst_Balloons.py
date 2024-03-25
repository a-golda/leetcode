from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]

        for balloon in points:
            start_balloon, end_balloon = balloon
            if start_balloon>end:
                arrows+=1
                end = end_balloon
            else:
                pass
        return arrows

print(Solution().findMinArrowShots(points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))



# 123456789123456
# [    ]
#  [     ]
#       [   ]
#          [    ]
