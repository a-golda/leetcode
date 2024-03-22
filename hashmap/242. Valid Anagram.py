class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(t)!=len(s)) or (len(s)==0) or (len(t)==0):
            return False

        i = 0
        while i<len(s):
            index = t.find(s[i])
            if index!=-1:
                t = t[:index]+t[index+1:]
                i+=1
            else:
                return False

        return i==len(s)


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if (len(t)!=len(s)) or (len(s)==0) or (len(t)==0):
            return False

        s_set = set(s)
        for l in s_set:
            if s.count(l)!=t.count(l):
                return False
            else:
                pass

        return True

print(Solution().isAnagram(s = "anagram", t = "nagaram"))