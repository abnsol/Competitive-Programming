class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows,cols = len(maze),len(maze[0])

        def inbound(i,j):
            return 0 <= i < rows and 0 <= j < cols

        q = deque([(entrance[0],entrance[1],1)]) # [i,j]
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        visited = set()
        border = []

        for i in range(rows):
            for j in range(cols):
                if (i in (0,rows - 1) or j in (0,cols - 1)) and entrance != [i,j] and maze[i][j] == ".":
                    border.append((i,j))


        while q:
            i,j,w = q.popleft()
            visited.add((i,j))
            n = len(q)
            for r,c in dirs:
                nr,nc = i + r,j + c
                if inbound(nr,nc) and maze[nr][nc] == "." and (nr,nc) not in visited:
                    
                    q.append((nr,nc,w + 1))
                    visited.add((nr,nc))

                if (nr,nc) in border:
                    return w
        
        return -1

'''
    + . + + + + +
    + . + . . . +
    + . + . + . +
    + . . . + . +
    + + + + + . +
   
'''


