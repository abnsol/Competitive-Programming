# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # should i update ans 
        # if not stk yes else prev = cur *= 2
        ans = 0
        stk = []
        for i in s:
            if i == ")":
                val = stk.pop()
                if stk:
                    if stk[-1] % 2 == 1: stk[-1] -= 1
                    stk[-1] += ((val) * 2)
                else:
                    ans += val
            else:
                stk.append(1)
        
        return ans
                    
        