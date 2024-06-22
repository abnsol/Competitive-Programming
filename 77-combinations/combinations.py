class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start,combination):
            if len(combination) == k:
                res.append(combination[:])
                return
            
            # making decision
            for i in range(start,n + 1):
                combination.append(i)
                backtrack(i + 1,combination)
                combination.pop()
        
        res = []
        backtrack(1,[])
        return res