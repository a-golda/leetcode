# from typing import List
#
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: x[0])
#         res = [intervals[0]]
#
#         for el in intervals[1:]:
#             should_append = False
#             merged = False
#             for i, inter in enumerate(res):
#                 inter_type = self.intersect(el, inter)
#                 if inter_type:
#                     res[i] = [min(el[0], inter[0]), max(el[1], inter[1])]
#                     merged = True
#                 else:
#                     should_append = True
#             if should_append and not merged:
#                 res.append(el)
#
#         final_res = []
#         for el in res:
#             if el not in final_res:
#                 final_res.append(el)
#             else:
#                 pass
#         return final_res
#
#     @staticmethod
#     def intersect(inter_0, inter_1):
#         if inter_1[0] >= inter_0[0] and inter_0[1] >= inter_1[1]: # 1[ ( ) ] or [( )]
#             return 1
#         elif inter_0[0] >= inter_1[0] and inter_1[1] >= inter_0[1]: # 2( [ ] ) or ([  ])
#             return 2
#         elif inter_1[0]<=inter_0[0] and inter_1[1]<=inter_0[1] and inter_0[0]<=inter_1[1]:  # 3( [) ]
#             return 3
#         elif inter_0[0]<=inter_1[0] and inter_0[1]<=inter_0[1] and inter_1[0]<=inter_0[1]:  # 4 [ (] )
#             return 4
#         else:
#             return False

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)

        return res

print(Solution().merge([[1,4],[0,4]]))