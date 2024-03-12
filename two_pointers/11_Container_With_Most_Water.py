# nlogn
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#
#         max_so_far = 0
#         i = 0
#         j = 1
#         while i<=len(height)-1:
#             while j<=len(height)-1:
#                 if min(height[i], height[j])*abs(i-j) > max_so_far:
#                     max_so_far=min(height[i], height[j])*abs(i-j)
#                 else:
#                     pass
#                 j+=1
#             i+=1
#             j=i+1
#         return max_so_far

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_so_far = 0

        while left!=right:
            potential_max = min(height[left], height[right]) * abs(left - right)
            max_so_far = max(max_so_far, potential_max)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_so_far


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))