# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         left_pointer = 0
#         right_pointer = len(nums)-1
#         middle_pointer = left_pointer+1
#
#         while left_pointer!=len(nums)-1:
#             while right_pointer!=0:
#                 while middle_pointer < right_pointer and middle_pointer>left_pointer:
#                     if left_pointer!=middle_pointer and middle_pointer!=right_pointer and left_pointer!=right_pointer:
#                         if nums[left_pointer] + nums[middle_pointer] + nums[right_pointer] == 0:
#                             final = sorted([nums[left_pointer], nums[middle_pointer], nums[right_pointer]])
#                             if final not in res:
#                                 res.append(final)
#                             middle_pointer+=1
#                         else:
#                             middle_pointer+=1
#                     else:
#                         middle_pointer+=1
#                 right_pointer -= 1
#                 middle_pointer = left_pointer+1
#             left_pointer += 1
#             right_pointer = len(nums)-1
#             middle_pointer = left_pointer + 1
#         return res


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        nums = sorted(nums)

        if len(nums)<3:
            return res
        else:
            pass

        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            else:
                pass

            left = i+1
            right = len(nums)-1
            while left<right:
                data = [nums[i], nums[left], nums[right]]
                sum_ = sum(data)
                if sum_==0:
                    res.append(data)
                    left += 1
                    right -= 1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    while nums[right] == nums[right + 1] and left < right:
                        right-=1
                elif sum_<0:
                    left+=1
                else:
                    right -= 1
        return res

print(Solution().threeSum([-1,0,1,2,-1,-4]))