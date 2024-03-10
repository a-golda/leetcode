# iteration like
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         len_nums = len(nums)
#
#         if len_nums==1:
#             return nums
#         else:
#             for i in range(1,k+1):
#                 nums = self.rotate_once(nums, len_nums)
#             return nums
#
#     def rotate_once(self, nums, len_nums):
#         current_to_move = nums[0]
#         for i in range(len_nums-1):
#             next = nums[i + 1]
#             nums[i+1] = current_to_move
#             current_to_move = next
#
#         nums[0] = next
#         return nums



# great and linear!
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         current_to_move = nums[0]
#         i = 0
#         j = 0
#         global_start = i
#         len_nums = len(nums)
#
#         if len_nums == 1 or k == 0 or len_nums == k:
#             return nums
#         else:
#             while global_start != len_nums:
#                 index_to_move = i + k
#                 if index_to_move >= len_nums:
#                     while index_to_move >= len_nums:
#                         index_to_move -= len_nums
#                 substitutable = nums[index_to_move]
#                 nums[index_to_move] = current_to_move
#                 current_to_move = substitutable
#                 global_start += 1
#                 i += k
#                 if index_to_move == j:
#                     j += 1
#                     i = j
#                     current_to_move = nums[i]
#             return nums


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        len_nums = len(nums)
        if len_nums == 1 or k == 0 or len_nums == k:
            return nums
        else:
            nums_left = nums[-k:]
            nums_right = nums[:-k]
            nums = nums_left + nums_right
            return nums

print(Solution().rotate([-1,-100,3,99], 2))