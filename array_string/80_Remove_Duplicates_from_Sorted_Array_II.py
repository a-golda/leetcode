class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-1)

        ofs = 0
        counter = 0
        for i in range(1, len(nums)-1):
            if nums[i-1-ofs] == nums[i-ofs]:
                counter += 1
                if counter >= 2:
                    nums.pop(i-1-ofs)
                    ofs += 1
                else:
                    pass

                if nums[i+1-ofs] != nums[i-ofs]:
                    counter = 0
                else:
                    pass
            else:
                pass

        k = len(nums)-1
        return k, nums

print(Solution().removeDuplicates([-2, -1]))