class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s = s.split(' ')
        dict_ = {}

        if (len(pattern)!=len(s)) or (len(s)==0) or (len(pattern)==0):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in dict_:
                dict_[pattern[i]] = s[i]
            else:
                if dict_[pattern[i]] != s[i]:
                    return False
                else:
                    pass

        if len(list(dict_.values()))!=len(set(dict_.values())):
            return False

        return True

print(Solution().wordPattern(pattern = "abba", s = "dog cat cat dog"))