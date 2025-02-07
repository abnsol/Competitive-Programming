# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # intialize hashset for each row,col,box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        #iterate through the board
        for r in range(9):
            for c in range(9):
                curNum = board[r][c]
                if curNum == ".":
                    continue
                
                box_idx = (r // 3) * 3 + (c // 3) 
                if curNum in rows[r] \
                or curNum in cols[c] or\
                curNum in boxs[box_idx]:
                    return False
                
                #update the rows,cols,boxs
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxs[box_idx].add(board[r][c])
        
        return True

        