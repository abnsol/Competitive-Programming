class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs =[(0,1),(-1,0),(0,-1),(1,0)]
        def inbound(i,j):
            return 0 <= i < len(board) and 0 <= j < len(board[0]) 

        def dfs(i,j):
            board[i][j] = 'c'
            for r,c in dirs:
                nr,nc = i + r,j + c
                if inbound(nr,nc) and board[nr][nc] == 'O':
                    dfs(nr,nc)

        n,m = len(board),len(board[0])
        for i in range(n):
            for j in range(m):
                bordercell = i in (0,n - 1) or j in (0,m - 1)
                if bordercell and board[i][j] == 'O':
                    dfs(i,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = "X"
                elif board[i][j] == 'c':
                    board[i][j] = 'O'

