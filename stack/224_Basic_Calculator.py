class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(' ', '')
        for i, el in enumerate(s):
            if el == ')':
                tmp_res = 0
                last_operation = None
                while len(stack)!=0 or stack[-1] != '(':
                    last = stack.pop()
                    if last not in ('(', ')', '+', '-'):
                        if last_operation is not None:
                            tmp_res = self.make_eval(last, tmp_res, last_operation)
                        else:
                            tmp_res = last
                    else:
                        if last in ('(', ')'):
                            continue
                        else:
                            last_operation = last
                stack.append(tmp_res)
            else:
                stack.append(el)

        if len(stack)!=1 and '(' not in stack and ')' not in stack:
            stack = eval(stack)
        else:
            raise ValueError

        return stack

    @staticmethod
    def make_eval(el1, el2, operation):
        if operation == '+':
            return el1 + el2
        elif operation == '-':
            return el1 - el2
        else:
            raise ValueError


print(Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)"))