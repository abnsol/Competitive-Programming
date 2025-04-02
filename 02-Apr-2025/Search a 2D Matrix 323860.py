# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix), len(matrix[0])
        start ,end = 0, row * col - 1

        while start <= end:
            mid = start + (end - start)//2

            if matrix[mid // col][mid % col] == target:
                return True
            elif matrix[mid // col][mid % col] > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return False