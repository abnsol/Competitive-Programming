class Solution {
    public int[] productExceptSelf(int[] nums) {
        int len = nums.length;
        int[] ans = new int[len];
        Arrays.fill(ans,1);

        for (int i = 1; i < len; i++){
            ans[i] = ans[i - 1] * nums[i - 1];
        }

        int right = 1;
        for (int j = len - 1; j > -1 ;j--){
            ans[j] *= right;
            right *= nums[j];
        }
        return ans;
    }
}