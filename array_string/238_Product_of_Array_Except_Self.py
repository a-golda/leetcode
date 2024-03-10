class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res_mult = 1
        final = []
        zero_counter = 0

        for num in nums:
            if num!=0:
                res_mult *= num
            else:
                zero_counter+=1

        if zero_counter==0:
            for num in nums:
                final.append(int(res_mult/num))
        elif zero_counter==1:
            for num in nums:
                if num==0:
                    final.append(int(res_mult))
                else:
                    final.append(0)
        else:
            for _ in nums:
                final.append(0)

        return final

print(Solution().productExceptSelf([-1,1,0,-3,3]))