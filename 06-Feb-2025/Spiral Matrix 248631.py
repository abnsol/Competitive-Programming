# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_len, col_len = len(matrix), len(matrix[0])
        visited = [[0] * col_len for _ in range(row_len)]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        dirs_idx = 0

        n = row_len * col_len
        i, j = 0, -1
        ans = []

        while len(ans) < n:
            nr, nc = i + dirs[dirs_idx][0], j + dirs[dirs_idx][1]
            while nr < row_len and nc < col_len and not visited[nr][nc]:
                ans.append(matrix[nr][nc])
                visited[nr][nc] = 1
                i ,j = nr, nc        
                nr, nc = i + dirs[dirs_idx][0], j + dirs[dirs_idx][1]
            dirs_idx = (dirs_idx + 1) % 4

        return ans        
            
                   