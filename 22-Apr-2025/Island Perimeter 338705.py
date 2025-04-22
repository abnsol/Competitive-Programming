# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]

        # not inbound or water = perimeter
        def inbound(i,j):
            return 0 <= i <= rows - 1 and 0 <= j <= cols - 1  
        
        visited = [[0] * cols for _ in range(rows)]
        ans = [0]
        
        def dfs(i,j):
            if not grid[i][j]:
                ans[0] += 1
                return

            visited[i][j] = 1

            for x,y in dirs:
                nr ,nc = i + x, j + y
                if not inbound(nr,nc):
                    ans[0] += 1
                elif not visited[nr][nc]:
                    dfs(nr,nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    dfs(i,j)
                    return ans[0]
        
        return 0
