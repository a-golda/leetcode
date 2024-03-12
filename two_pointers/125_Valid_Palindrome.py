class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([l.lower() for l in s if any(l.isalpha(), l.isdigit())])
        if s=='':
            return True
        else:
            pass

        for i in range(int(len(s)/2) + 1):
            if s[i] == s[-i-1]:
                if i == round(len(s)/2):
                    return True
                else:
                    pass
            else:
                break

        return False

print(Solution().isPalindrome("0P"))