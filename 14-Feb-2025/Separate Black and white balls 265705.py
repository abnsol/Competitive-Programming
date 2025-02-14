# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        one_cnt = ans = 0
        for r in range(len(s)):
            if s[r] == "1":
                one_cnt += 1
            else:
                ans += one_cnt
        
        return ans

        