# class Solution:
#     def isValid(self, s: str) -> bool:
#         l = len(s)
#         i = 0
#         while i <= l +1:
#             s = s.replace('{}', '')
#             s = s.replace('[]', '')
#             s = s.replace('()', '')
#             if len(s)==0:
#                 return True
#             else:
#                 i += 1
#
#         return len(s)==0


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'(':')', '{':'}', '[':']'}
        stack = []

        for symbol in s:
            if symbol in hashmap:
                stack.append(symbol)
            else:
                if len(stack)!=0 and symbol == hashmap[stack.pop()]:
                    pass
                else:
                    return False

        return len(stack) == 0


print(Solution().isValid('[()]'))