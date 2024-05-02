class Solution {
    public int findMaxK(int[] nums) {
        Arrays.sort(nums);
        int l = 0, r = nums.length - 1;

        while (l < r){
            if (nums[l] > 0 || nums[r] < 0) return -1;
            else if(Math.abs(nums[l]) > nums[r]) l++;
            else if(Math.abs(nums[l]) < nums[r]) r--;
            else return nums[r];
        }return -1;
    }
}