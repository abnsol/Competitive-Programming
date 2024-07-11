class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1

        dirs = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]
        path = 1
        q = deque([(0,0)])
        grid[0][0] = 1

        while q:
            length = len(q)
            for i in range(length):
                i,j = q.popleft()

                if i == j == n - 1:
                    return path

                for r,c in dirs:
                    nr = i + r
                    nc = j + c
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                        grid[nr][nc] = 1
                        q.append((nr,nc))
                
            path += 1
        return -1


