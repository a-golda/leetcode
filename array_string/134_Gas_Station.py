# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         """
#         :type gas: List[int]
#         :type cost: List[int]
#         :rtype: int
#         """
#
#         if sum(gas)<sum(cost) or sum(gas)<len(cost):
#             return -1
#         elif max(gas)>=len(cost) and len(gas)==sum(gas):
#             return gas.index(max(gas))
#         else:
#             pass
#
#         for start_pos in range(len(cost)):
#             current_tank_cap = 0
#             for i in range(len(cost)):
#                 act_pos = start_pos + i
#                 if act_pos >= len(cost):
#                     act_pos -= len(cost)
#                 else:
#                     pass
#                 current_tank_cap += gas[act_pos]
#                 current_tank_cap -= cost[act_pos]
#                 if current_tank_cap < 0:
#                     break
#                 else:
#                     pass
#             if current_tank_cap < 0:
#                 pass
#             else:
#                 return start_pos
#         return -1


class Solution:
    def canCompleteCircuit(self, gas, cost):
        ans = 0
        summ = 0

        net = sum(gas) - sum(cost)

        # Try to start from each index.
        for i in range(len(gas)):
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                ans = i + 1  # Start from the next index.

        return -1 if net < 0 else ans


print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))



[1, 3, 0, 0, 1]
[1, 1, 1, 1, 1]