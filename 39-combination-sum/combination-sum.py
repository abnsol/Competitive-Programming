class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(start,comb):
            if start >= len(candidates) or sum(comb) > target:
                return
            
            if sum(comb) == target:
                res.append(comb[:])
                return
        
            comb.append(candidates[start])
            bt(start,comb)
            comb.pop()
            bt(start + 1,comb)
        
        bt(0,[])
        return res