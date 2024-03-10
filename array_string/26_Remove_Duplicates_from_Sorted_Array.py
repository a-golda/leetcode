class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ofs = 0
        for i in range(1, len(nums)):
            if nums[i-1-ofs] == nums[i-ofs]:
                nums.pop(i-1-ofs)
                ofs+=1
            else:
                pass

        k = len(nums)
        return k

print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))