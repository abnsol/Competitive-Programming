# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        visited = set()
        count = 0

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i,j,cnt):
            if (i,j) in visited or not inbound(i,j) or grid[i][j] == 0:
                return cnt
                        
            visited.add((i,j))
            cnt += 1
            for r,c in dirs:
                cnt += dfs(i + r,j + c,0)  

            return cnt

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] != 0:
                    count = max(count,dfs(i,j,0))

        return count