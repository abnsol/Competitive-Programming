class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = set()
        def backtrack(num,arr):
            if len(arr) >= k:
                ans.add(tuple(arr)) 
                return
            
            if num > n:
                return 
            
            backtrack(num + 1,arr)
            backtrack(num + 1,arr + [num])

            return 
        backtrack(1,[])
        return ans