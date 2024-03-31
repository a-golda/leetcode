from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for el in tokens:
            if el not in ('*', '/', '+', '-'):
                stack.append(el)
            else:
                assert len(stack)>=2
                res = str(int(eval(stack[-2] + el + stack[-1])))
                if el == '/':
                    res = str(int(float(res) - float(res)%1))
                else:
                    pass
                stack.pop()
                stack.pop()
                stack.append(res)


        assert len(stack)==1
        return int(stack[0])

print(Solution().evalRPN(tokens =["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))