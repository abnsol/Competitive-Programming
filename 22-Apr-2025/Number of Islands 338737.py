# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not in visited or not water explore them
        # exploring them add them to visited
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]

        def inbound(i,j):
            return 0 <= i <= rows - 1 and 0 <= j <= cols - 1

        def dfs(i,j):
            grid[i][j] = 0

            for x,y in dirs:
                nr, nc = i + x, j + y
                if inbound(nr,nc) and int(grid[nr][nc]):
                    dfs(nr,nc)
                
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if int(grid[i][j]):
                    ans += 1
                    dfs(i,j)
        
        return ans

        