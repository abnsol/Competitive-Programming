# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        ans = [0] * n
        for i in range(n):
            ans[indices[i]] = s[i]
        
        return "".join(ans)
        