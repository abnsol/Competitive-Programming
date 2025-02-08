# Problem: Largest Local Values in a Matrix - https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        for i in range(1,n - 1):
            local_max = []
            for j in range(1,n - 1):
                ans = grid[i][j]
                for dx,dy in dirs:
                    nr,nc = i + dx,j + dy
                    ans = max(ans,grid[nr][nc])
                local_max.append(ans)
            res.append(local_max)
        
        return res

                        