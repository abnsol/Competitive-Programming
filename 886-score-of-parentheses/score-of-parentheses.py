class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = openb = idx = 0
        while idx < len(s):
            if s[idx] == "(":
                openb += 1
                idx += 1
            else:
                score += 2 ** (openb - 1)
                while idx < len(s) and s[idx] == ')':
                    openb -= 1
                    idx += 1
            
        return score
        