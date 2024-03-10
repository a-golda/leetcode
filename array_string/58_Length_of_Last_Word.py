class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip(' ')
        res = 0

        if ' ' not in s:
            return len(s)
        else:
            for i in (range(len(s)-1, 0, -1)):
                if s[i]!=' ':
                    res+=1
                else:
                    break
            return res

print(Solution().lengthOfLastWord("luffy is still joyboy"))