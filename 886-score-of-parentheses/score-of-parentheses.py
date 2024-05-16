class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = idx = 0
        stack = []
        while idx < len(s):
            if s[idx] == "(":
                stack.append(s[idx])
                idx += 1
            else:
                score += 2 ** (len(stack) - 1)
                while idx < len(s) and s[idx] == ')':
                    stack.pop()
                    idx += 1
            
        return score
        