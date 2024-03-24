# class Solution:
#     def containsNearbyDuplicate(self, nums, k: int) -> bool:
#         for i in range(len(nums)):
#             for (j) in range(i+1, i+k+1):
#                 if j< len(nums):
#                     if nums[i]==nums[j] and abs(i-j)<=k:
#                         return True
#                     else:
#                         pass
#                 else:
#                     break
#
#         return False

class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict_ = {}

        for i in range(len(nums)):
            if (nums[i] in dict_.keys()) and (abs(dict_[nums[i]]-i)<=k):
                return True
            else:
                dict_[nums[i]] = i

        return False


print(Solution().containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))