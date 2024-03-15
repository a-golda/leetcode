# class Solution(object):
#     def minSubArrayLen(self, target, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = 0
#
#         for i in range(len(nums)):
#             left = i
#             right = len(nums)
#             while left<=right:
#                 subarray = nums[left:right]
#                 if sum(subarray)>=target:
#                     if len(subarray)<res:
#                         res = len(subarray)
#                     elif res==0:
#                         res = len(subarray)
#                     else:
#                         pass
#                 else:
#                     pass
#                 right-=1
#
#         return res

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        window_sum = 0
        min_l = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_l = min(min_l, right - left)
                window_sum -= nums[left]
                left += 1

        return min_l+1 if min_l!=float('inf') else 0


print(Solution().minSubArrayLen(7, [2,3,1,2,4,3]))