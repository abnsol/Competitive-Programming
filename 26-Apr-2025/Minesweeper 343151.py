# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        r,c = click[0],click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        visited = set()
        dirs = [(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1)]

        def inbound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0])
        
        
        def cnt_mine(i, j):
            count = 0
            for r, c in dirs:
                nr, nc = i + r, j + c
                if inbound(nr, nc) and board[nr][nc] == 'M':
                    count += 1
            return count

        def dfs(i, j):
            if not inbound(i, j) or (i, j) in visited:
                return
            
            visited.add((i, j))
            cnt = cnt_mine(i, j)
            
            if cnt > 0:
                board[i][j] = str(cnt)
            else:
                board[i][j] = 'B'
                for r, c in dirs:
                    nr, nc = i + r, j + c
                    if inbound(nr, nc) and board[nr][nc] == 'E':
                        dfs(nr, nc)

        dfs(r, c)
        return board
                

'''
click 
    if mine - change to x then return
    if unrevealed E - 
        reveal if no adjacents change to B then dfs reveal
               if adjacent revealed += 1 return 
'''