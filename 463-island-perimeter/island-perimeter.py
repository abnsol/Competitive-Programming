class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        visited = set()

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])
        
        def dfs(i,j):
            if not inbound(i,j) or grid[i][j] == 0:
                return 1

            if (i,j) in visited:
                return 0

            visited.add((i,j))
            perimeter = 0
            for r,c in dirs:
                perimeter += dfs(i + r,j + c)
            
            return perimeter
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    return dfs(i,j)


        






















































            