class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        x1, y1 = -1, -1
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    x1, y1 = i, j
                    break
        
        
        def dfs(x, y):
            grid[x][y] = 2
            q.append((x, y))
            for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                    dfs(r, c)
        

        q = []
        dfs(x1, y1)
        
        distance = 0
        while q:
            queue = []
            for x, y in q:
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < n and 0 <= c < n:
                        if grid[r][c] == 1:
                            return distance
                        elif grid[r][c] == 0:
                            queue.append((r, c))
                            grid[r][c] = -1

            
            q = queue
            distance += 1