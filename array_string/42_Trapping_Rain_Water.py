# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         bounds_min = []
#         for i in range(1,len(height)-1):
#             current_height = height[i]
#
#             l = i
#             left = height[l]
#             while l!=0:
#                 if height[l-1]>left:
#                     left = height[l-1]
#                     l = l-1
#                 else:
#                     l = l-1
#
#             r = i
#             right = height[r]
#             while r!=len(height)-1:
#                 if height[r+1]>right:
#                     right = height[r+1]
#                     r+=1
#                 else:
#                     r+=1
#
#             l_v = 0
#             if left-current_height > 0:
#                 l_v = left-current_height
#             else:
#                 pass
#
#             r_v = 0
#             if right-current_height > 0:
#                 r_v = right-current_height
#             else:
#                 pass
#
#             bounds_min.append(min(l_v, r_v))
#
#         return sum(bounds_min)


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         bounds_min = 0
#
#         for i in range(1,len(height)-1):
#             current_height = height[i]
#
#
#             l = i
#             left = height[l]
#             while l!=0:
#                 if height[l-1]>left:
#                     left = height[l-1]
#                     l = l-1
#                 else:
#                     l = l-1
#
#             r = i
#             right = height[r]
#             while r!=len(height)-1:
#                 if height[r+1]>right:
#                     right = height[r+1]
#                     r+=1
#                 else:
#                     r+=1
#
#             l_v = 0
#             if left-current_height > 0:
#                 l_v = left-current_height
#             else:
#                 pass
#
#             r_v = 0
#             if right-current_height > 0:
#                 r_v = right-current_height
#             else:
#                 pass
#
#             bounds_min += min(l_v, r_v)
#
#         return bounds_min


# class Solution(object):
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         valume = 0
#         left = height[0]
#         right = height[-1]
#
#         for i in range(1, len(height) - 1):
#             current_height = height[i]
#
#             if current_height>left:
#                 left = current_height
#             else:
#                 pass
#
#             if right < height[i]:
#                 right = max(height[i:])
#             else:
#                 pass
#
#             l_v = max(0, left - current_height)
#             r_v = max(0, right - current_height)
#             valume += min(l_v, r_v)
#
#         return valume


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_ = max(height)
        max_index = height.index(max_)
        volume = 0

        current = height[0]
        for i in range(1, max_index):
            if height[i]<current:
                volume+=current-height[i]
            else:
                current=height[i]

        current = height[-1]
        for i in range(len(height)-2, max_index, -1):
            if height[i] < current:
                volume += current - height[i]
            else:
                current = height[i]

        return volume


print(Solution().trap([4,2,0,3,2,5]))




# we need to find neares left and right maximums for each point - and take a min of these two.