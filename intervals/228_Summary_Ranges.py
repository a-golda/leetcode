class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        final = []
        start_index = 0
        end_index = 0

        for i, el in enumerate(nums):
            if i+1<len(nums):
                if nums[i + 1] - el == 1:
                    end_index+=1
                else:
                    final.append([start_index, end_index])
                    start_index = i+1
                    end_index = i+1
            else:
                final.append([start_index, end_index])

        for i, el in enumerate(final):
            if el[0]==el[1]:
                el = str(nums[el[0]])
            else:
                el = f'{nums[el[0]]}->{nums[el[1]]}'
            final[i] = el

        return final

print(Solution().summaryRanges(nums = [0,2,3,4,6,8,9]))