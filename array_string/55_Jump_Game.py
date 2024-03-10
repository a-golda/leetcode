# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         current_pos = 0
#         current_length = nums[0]
#
#         for i in range(len(nums)-1):
#             if nums[i]!=0:
#                 current_pos += 1
#                 current_length = nums[i]
#             else:
#                 current_length -= 1
#                 if current_length>0:
#                     current_pos += 1
#                 else:
#                     pass
#
#         return current_pos==len(nums)-1


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        target_pos = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i+nums[i]>=target_pos:
                target_pos=i

        return target_pos==0
