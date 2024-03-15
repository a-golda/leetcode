class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        total_window_len = len(words[0])*len(words)
        res = []
        left = 0
        right = left+total_window_len
        current = s[left:right]

        while right<len(s):
            tester = list(words)

            for i in range(len(words)):
                one_word = current[i*len(words[0]):(i+1)*len(words[0])]
                if one_word in tester:
                    tester.remove(one_word)
                else:
                    break

            if len(tester)==0:
                res.append(left)
            else:
                pass

            left+=1
            right+=1

        return res

print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))