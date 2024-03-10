class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        final_dict = {
            nums[0]:0
        }

        for el in nums:
            if el in final_dict.keys():
                final_dict[el] = final_dict[el]+1
                if final_dict[el]>len(nums)/2:
                    return el
                else:
                    pass
            else:
                final_dict[el] = 1

        return final_dict


print(Solution().majorityElement([3,2,3]))

