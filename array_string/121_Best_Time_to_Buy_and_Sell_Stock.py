# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         min_p, max_p = prices[0], prices[0]
#         min_p_index, max_p_index = 0, 0
#         diff = []
#
#         for i, p in enumerate(prices):
#             if p < min_p:
#                 min_p, max_p = p, p
#                 min_p_index, max_p_index = i, i
#             else:
#                 pass
#
#             if p > max_p:
#                 max_p=p
#                 max_p_index = i
#             else:
#                 pass
#
#             if max_p_index > min_p_index:
#                 diff.append(max_p-min_p)
#             else:
#                 pass
#
#         if len(diff)==0:
#             return 0
#         else:
#             res = 0
#             for d in diff:
#                 if d>res:
#                     res = d
#             return res


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p, max_p = prices[0], prices[0]
        min_p_index, max_p_index = 0, 0
        diff = 0

        for i, p in enumerate(prices):
            if p < min_p:
                min_p, max_p = p, p
                min_p_index, max_p_index = i, i
            else:
                pass

            if p > max_p:
                max_p=p
                max_p_index = i
            else:
                pass

            if max_p_index > min_p_index and max_p-min_p>diff:
                diff = max_p-min_p
            else:
                pass

        return diff



print(Solution().maxProfit([7,2,4,1]))