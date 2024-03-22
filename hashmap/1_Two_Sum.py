class Solution:
    def twoSum(self, nums, target: int):
        dict_ = {}

        for i, n in enumerate(nums):
            if target-n in dict_:
                return [i, dict_[target-n]]
            else:
                dict_[n] = i



print(Solution().twoSum(nums = [3,3], target = 6))