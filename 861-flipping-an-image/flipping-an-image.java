class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int[] row: image){
            int left = 0, right = row.length -1;
            while (left <= right){
                int temp = row[left] ^ 1;
                row[left] = row[right] ^ 1;
                row[right] = temp;
                left += 1;
                right -= 1;
            }
        }
        return image;
    }
}