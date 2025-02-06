# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col, row = len(matrix), len(matrix[0])
        transpose = [[0]* col for i in range(row)]
        for i in range(row):
            for j in range(col):
                transpose[i][j] = matrix[j][i]

        return transpose 

              