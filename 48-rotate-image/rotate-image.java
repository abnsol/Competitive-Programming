class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i = 0; i < 3; i++){
            transpose(matrix,n);
            reverse(matrix,n);
        }
    }
    static void transpose(int[][] matrix,int n){
        for (int i = 0; i < n; i++){
            for(int j = i; j < n; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }

    static void reverse(int[][] matrix,int n){
        for (int i  = 0; i < n; i++){
            for (int j = 0, k = n - 1; j < k; j++ , k--){
                int temp = matrix[j][i];
                matrix[j][i] = matrix[k][i];
                matrix[k][i] = temp;
            }
        }
    }
}