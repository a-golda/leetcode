# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         citations = [c for c in citations if c!=0]
#         enough = []
#
#         for i, amount_i in enumerate(citations):
#             current_h = 0
#             for amount_j in citations:
#                 if amount_j>=amount_i:
#                     current_h+=1
#                 else:
#                     pass
#
#                 if current_h>=amount_i:
#                     enough.append(amount_i)
#                 else:
#                     pass
#
#         if len(enough)==0:
#             res = len(citations)
#         else:
#             res = enough[0]
#
#         for k in enough:
#             if k>res:
#                 res=k
#             else:
#                 pass
#
#         return res


# class Solution(object):
#     def hIndex(self, citations):
#         """
#         :type citations: List[int]
#         :rtype: int
#         """
#         return self.simple_index(min([len(citations), max(citations)]), citations)
#
#     def simple_index(self, h_index, citations):
#         counter = 0
#         for c in citations:
#             if c >= h_index:
#                 counter += 1
#             else:
#                 pass
#
#         if counter >= h_index:
#             return h_index
#         elif h_index==0:
#             return 0
#         else:
#             return self.simple_index(h_index - 1, citations)
#
#
#         # return max([h_index, 0])


class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        c = sorted(citations, key = lambda x: -x)
        res = 0
        while res < len(c):
            if c[res] < res+1:
                break
            res += 1
        return res


print(Solution().hIndex([1,7,9,4]))