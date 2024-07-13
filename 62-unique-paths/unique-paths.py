class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dirs = [(0,1),(1,0)]
        def inbound(i,j):
            return i < m and j < n

        memo = {}
        def dfs(i,j):
            if i == m - 1 and j == n - 1:
                return 1
            
            if not inbound(i,j):
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
                
            
            path = 0
            for r,c in dirs:
                path += dfs(i + r,j + c)
            
            memo[(i,j)] = path
            return path

        return dfs(0,0)
