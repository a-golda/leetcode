class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_l = -1

        current = ''
        for right in range(len(s)):
            while (s[right] in current) and left<right:
                current = current[1:]
                left+=1
            if s[right] not in current:
                current += s[right]
                max_l = max(max_l, right - left +1)
            else:
                pass

        return max_l if max_l!=-1 else 0

print(Solution().lengthOfLongestSubstring(""))