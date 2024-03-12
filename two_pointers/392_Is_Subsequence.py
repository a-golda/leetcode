class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        res = 0

        if len(s)==0:
            return True
        elif len(t)==0:
            return False

        for i in range(len(t)):
            if res>=len(s):
                break
            elif t[i]==s[res]:
                res+=1
            else:
                pass

        return res>=len(s)

print(Solution().isSubsequence("b", "abc"))
