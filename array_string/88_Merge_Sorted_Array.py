# class Solution(object):
#     @staticmethod
#     def merge(nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         os=0
#         for i in range(m + n):
#             if len(nums2) == 0:
#                 break
#             l1 = nums1[i+os]
#             l2 = nums2[0]
#             if l1 >= l2 or l1==0:
#                 nums1.insert(i+os, nums2.pop(0))
#                 if l1!=0:
#                     os += 1
#             else:
#                 pass
#         nums1 = nums1[:n + m]
#         print(nums1)

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i-=1
                k-=1
            else:
                nums1[k] = nums2[j]
                j-=1
                k-=1
        return nums1

print(Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3))
