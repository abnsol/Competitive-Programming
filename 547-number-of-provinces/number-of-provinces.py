class Solution:
    def findCircleNum(self, grid: List[List[int]]) -> int:
        visited =set()
        cnt = 0
        
        def dfs(idx):
            if idx in visited:
                return 
            
            visited.add(idx)
            for i in range(len(grid[0])):
                if grid[idx][i] != 0:
                    dfs(i)


        for idx in range(len(grid)):
            if idx not in visited:
                cnt += 1
                dfs(idx)

        return cnt
                