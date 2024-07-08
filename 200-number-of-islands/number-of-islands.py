class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,-1),(-1,0),(0,1),(1,0)]
        visited = set()
        count = 0

        def inbound(i,j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i,j):
            if (i,j) in visited or not inbound(i,j) or grid[i][j] == '0':
                return
                        
            visited.add((i,j))
            for r,c in dirs:
                dfs(i + r,j + c)  
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] != '0':
                    count += 1
                    dfs(i,j)
        return count

             