class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        left_pointer = 0
        right_pointer = len(nums)-1
        middle_pointer = left_pointer+1

        while left_pointer!=len(nums)-1:
            while right_pointer!=0:
                while middle_pointer < right_pointer and middle_pointer>left_pointer:
                    if left_pointer!=middle_pointer and middle_pointer!=right_pointer and left_pointer!=right_pointer:
                        if nums[left_pointer] + nums[middle_pointer] + nums[right_pointer] == 0:
                            final = sorted([nums[left_pointer], nums[middle_pointer], nums[right_pointer]])
                            if final not in res:
                                res.append(final)
                            middle_pointer+=1
                        else:
                            middle_pointer+=1
                    else:
                        middle_pointer+=1
                right_pointer -= 1
                middle_pointer = left_pointer+1
            left_pointer += 1
            right_pointer = len(nums)-1
            middle_pointer = left_pointer + 1
        return res

print(Solution().threeSum([3,0,-2,-1,1,2]))