class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        i = 0
        while all([strs[0][:i]==str_[:i] for str_ in strs]):
            i+=1
            if len(strs[0]) == i-1:
                break
        return strs[0][:i-1]

print(Solution().longestCommonPrefix([""]))