class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        left = 0
        right = 0
        min_so_far = len(s)+1
        min_so_far_l, min_so_far_r = 0,0

        res_counter = len(t)

        while right <= len(s):
            right +=1
            current = s[left:right]
            while left < right and self.check(current, t):
                if min_so_far>=right - left + 1:
                    min_so_far = right - left + 1
                    min_so_far_l, min_so_far_r = left, right
                else:
                    pass
                left+=1
                current = s[left:right]
        return s[min_so_far_l:min_so_far_r]


    @staticmethod
    def check(str_, substr_):
        if len(substr_)>len(str_):
            return False

        str_ = list(str_)
        tmp_substr_ = list(substr_)
        for letter in substr_:
            if letter in str_:
                tmp_substr_.remove(letter)
                str_.remove(letter)
            else:
                break

        if len(tmp_substr_)==0:
            return True
        else:
            return False

print(Solution().minWindow("acbbaca", "aba"))