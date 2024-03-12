class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        while i < len(numbers)-1:
            el_0 = numbers[i]
            for j in range(i+1,len(numbers)):
                el_1 = numbers[j]
                if el_0+el_1 == target:
                    return [i+1, j+1]
                elif el_0+el_1>target:
                    break
                else:
                    pass
            while numbers[i]==numbers[i+1]:
                i+=1
            i += 1
