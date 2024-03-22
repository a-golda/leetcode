class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = []
        strs_sets = []
        skip_list = []

        for str_ in strs:
            hist = {}
            for l in str_:
                if l not in hist:
                    hist[l] = (f'{l}{str_.count(l)}')
                else:
                    pass
            strs_sets.append(hist)

        for i, str_ in enumerate(strs):
            tmp_res = []
            for j, str_set in enumerate(strs_sets):
                if strs_sets[i] == str_set and j not in skip_list:
                    tmp_res.append(strs[j])
                    skip_list.append(j)
                else:
                    pass
            skip_list.append(i)
            if len(tmp_res)!=0:
                res.append(tmp_res)
            else:
                pass

        return res


print(Solution().groupAnagrams(strs = ["ddddddddddg","dgggggggggg"]))