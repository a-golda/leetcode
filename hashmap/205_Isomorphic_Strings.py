class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if (len(s)!=len(t)) or (len(s)==0) or (len(t)==0):
            return False
        else:
            pass

        dict_ = {}
        for i in range(len(s)):
            if s[i] not in dict_.keys():
                dict_[s[i]] = t[i]
            else:
                if dict_[s[i]] == t[i]:
                    pass
                else:
                    return False

        if len(list(dict_.values()))!=len(set(dict_.values())):
            return False

        return True


print(Solution().isIsomorphic(s = "badc", t = "baba"))