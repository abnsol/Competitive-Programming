class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ")":
                word = ''
                while stack[-1] != '(':
                    word += stack.pop()
                stack.pop()
                for j in word:
                    stack.append(j)
            else:
                stack.append(i)
        
        return ''.join(stack)