class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix), len(matrix[0])
        start ,end = 0, row * col - 1

        while start <= end:
            mid = start + (end - start)//2
            curr_row = mid // col
            curr_col = mid % col
            mid_val = matrix[curr_row][curr_col]

            if mid_val == target:
                return True
            elif mid_val > target:
                end = mid - 1
            else:
                start = mid + 1
            
        return False