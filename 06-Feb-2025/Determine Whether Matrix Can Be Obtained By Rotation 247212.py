# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def transpose(self,matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if i > j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp  
        
        return matrix

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # transpose, rotate

        n = len(mat)
        transpose = mat
        for i in range(4):
            transpose = self.transpose(transpose)
            for i in range(n):
                transpose[i] = transpose[i][::-1]

            if transpose == target:
                return True        
        return False

        