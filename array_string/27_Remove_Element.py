class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        del_arr = []
        for i in range(len(nums)):
            if nums[i] == val:
                del_arr.append(i)
                k += 1

        ofs = 0
        for j in del_arr:
            nums.pop(j - ofs)
            ofs += 1

        print(nums)
        return k


Solution().removeElement([0,1,2,2,3,0,4,2], 2)