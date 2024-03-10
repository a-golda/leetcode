class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split(' ')
        res = ' '.join([word for word in strs[::-1] if word != ''])
        return res

print(Solution().reverseWords("  hello world  "))