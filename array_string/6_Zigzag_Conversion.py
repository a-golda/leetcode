class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        max_skip_symbols = numRows*2 - 1
        res=''

        i = 0
        j = 0
        while len(res)!=len(s):
            if i>len(s)-1:
                j+=1
                i=j
            res+=s[i]
            i+=max_skip_symbols-1

        return res

print(Solution().convert("PAYPALISHIRING", 3))



# 1 - 1
# 2 - 3
# 3 - 5
# 4 - 7

# None
# 2 - 3
# 3 - 5
# 4 - 7
# 5 - 9

# None
# None
# 3 - 5
#





