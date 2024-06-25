class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # simulation
        ROWS,COLS = len(board),len(board[0])
        path = set() # to not go back if visited

        def bt(r,c,i):
            if i == len(word):
                return True
            
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                word[i] != board[r][c] or
                (r,c) in path):
                return False
            
            path.add((r,c))
            
            # the simulation(go down,go up,go right,go left)
            res = (bt(r + 1,c,i + 1) or bt(r - 1,c,i + 1) or
                  bt (r,c + 1,i + 1) or bt(r,c - 1,i + 1))
            
            path.remove((r,c))
            return res
        
        # starting at every letter in the grid
        for r in range(ROWS):
            for c in range(COLS):
                if bt(r,c,0):
                    return True
        
        return False
