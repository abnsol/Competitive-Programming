class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        res = n + 1
        cntW = 0

        for _ in range(k):
            if blocks[_] == "W":
                cntW += 1
        
        res = min(res,cntW)
        l = 0
        for r in range(k,n):
            if blocks[r] == "W":
                cntW += 1
            
            if blocks[l] == "W":
                cntW -= 1

            l += 1
            res = min(res,cntW)
        
        return res
            




'''
cntB = 4
cntW = 3
fixed sw
'''