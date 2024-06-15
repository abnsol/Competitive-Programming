class Solution:
    def minMoves(self, t: int, md: int) -> int:
        s, ans = 1, 0 
        while md > 0:
            double = 2**md
            ans += ((t // double) - s) + 1
            if t >= double:
                s = (t // double) * 2
            md -= 1
                    
        ans += t - s
        return ans


        

