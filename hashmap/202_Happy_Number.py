class Solution:
    NUMBERS_SEEN = []

    def isHappy(self, n: int) -> bool:
        new = [int(i)**2 for i in str(n)]
        sum_new = sum(new)
        if sum_new == 1:
            return True
        else:
            if Solution.NUMBERS_SEEN.count(sum_new)>1:
                return False
            else:
                Solution.NUMBERS_SEEN.append(sum_new)
                return Solution().isHappy(sum_new)


print(Solution().isHappy(23))