class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        def transpose(matrix,n):
            for i in range(n):
                for j in range(i,n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        def reverse(matrix,n):
            for i in range(n):
                k = n - 1
                j = 0
                while j < k:
                    matrix[j][i], matrix[k][i] = matrix[k][i], matrix[j][i]
                    j += 1
                    k -= 1
            
        for i in range(3):
            transpose(matrix,n)
            reverse(matrix,n)

        