# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        spl = s.split()
        res = []
        max_len = 0
        n = len(spl)
        for i in range(n):
            max_len = max(max_len,len(spl[i])) 
        
        for i in range(max_len):
            ans = []
            for j in range(n):
                if i >= len(spl[j]):
                    ans.append(" ")
                else:
                    ans.append(spl[j][i])
            res.append("".join(ans).rstrip())
        
        return res