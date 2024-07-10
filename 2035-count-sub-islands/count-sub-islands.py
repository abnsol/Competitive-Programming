class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cnt = 0
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        def inbound(i,j):
            return 0 <= i < len(grid1) and 0 <= j < len(grid1[0])

        def dfs(i,j):
            if not inbound(i,j) or grid2[i][j] == 0:
                return 
            
            grid2[i][j] = 0
            for r,c in dirs:
                dfs(i + r,j + c)
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1 and grid1[i][j] == 0:
                    dfs(i,j)
        
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j] == 1:
                    dfs(i,j)
                    cnt += 1
                
        return cnt

        