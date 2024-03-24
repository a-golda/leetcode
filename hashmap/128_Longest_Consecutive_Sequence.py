class Solution:
    def longestConsecutive(self, nums) -> int:
        if len(nums) == 0:
            return 0
        else:
            pass

        nums_set = set(nums)
        res = 1

        for i in range(len(nums)):
            if nums[i] - 1 not in nums_set:
                tmp_counter = 1
                while nums[i] + tmp_counter in nums_set:
                    tmp_counter += 1
                res = max(res, tmp_counter)
        return res

print(Solution().longestConsecutive([0, 0, 1, -1]))