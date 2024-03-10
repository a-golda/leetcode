class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_p, min_p = prices[0], prices[0]
        max_p_index, min_p_index = 0, 0
        diff = 0

        for i, p in enumerate(prices):
            if p < min_p:
                max_p, min_p = p, p
                max_p_index, min_p_index = i, i
            else:
                pass

            if p > max_p:
                max_p = p
                max_p_index = i
            else:
                pass

            if max_p_index>min_p_index and max_p-min_p>0:
                diff += max_p-min_p
                max_p, min_p = p, p
                max_p_index, min_p_index = i, i
            else:
                pass

        return diff


print(Solution().maxProfit([7,6,4,3,1]))
