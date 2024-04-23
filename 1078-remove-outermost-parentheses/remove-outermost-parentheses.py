class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        cnt = 0

        for char in s:
            if char == "(":
                cnt += 1
                if cnt > 1:
                    ans.append(char)
            else:
                cnt -= 1
                if cnt > 0:
                    ans.append(char)
            
        return "".join(ans)