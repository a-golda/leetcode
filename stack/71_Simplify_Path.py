class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for step in path.split('/'):
            if step == '..':
                if len(stack)!=0:
                    stack.pop()
                else:
                    continue
            elif step in ('.', ''):
                continue
            else:
                stack.append(step)

        return '/' + '/'.join(stack)



print(Solution().simplifyPath("/..."))
