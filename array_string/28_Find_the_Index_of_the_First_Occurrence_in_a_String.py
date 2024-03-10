# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         return haystack.find(needle)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i = 0
        j = 0
        res = -1

        while i<=len(haystack)-1:
            while j<=len(needle)-1:
                if i > len(haystack)-1:
                    break
                elif haystack[i]==needle[j]:
                    i+=1
                    j+=1
                else:
                    i-=j
                    j=0
                    break
            if j==len(needle):
                res = i-j
                break
            else:
                i+=1
        return res



print(Solution().strStr("a", "a"))