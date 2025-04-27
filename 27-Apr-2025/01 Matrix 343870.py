# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat),len(mat[0])
        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col

        distance = [[-1] * col for _ in range(row)]
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        q = deque()

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    q.append((i,j))
        
        while q:
            i,j = q.popleft()
            for r,c in dirs:
                nr,nc = i + r,j + c
                if inbound(nr,nc) and distance[nr][nc] == -1:
                    distance[nr][nc] = distance[i][j] + 1
                    q.append((nr,nc))
        
        return distance

