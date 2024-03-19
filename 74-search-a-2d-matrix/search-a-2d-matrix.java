class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length , col = matrix[0].length;
        int start = 0, end = row * col - 1;

        while (start <= end){
            int mid = start + (end - start)/2;

            if (matrix[mid / col][mid % col] == target){
                return true;
            }
            else if(matrix[mid / col][mid % col] > target){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        return false;
    }
}