class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] ans = new int[len];
        Arrays.fill(ans,1);

        int left = 1;
        for (int i = 0; i < len; i++){
            ans[i] = left;
            left *= nums[i];
        }

        int right = 1;
        for (int j = len - 1; j > -1 ;j--){
            ans[j] *= right;
            right *= nums[j];
        }
        return ans;
    }
}