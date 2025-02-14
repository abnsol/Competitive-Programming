# Problem: Rotate Array - https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_elem = {}
        n = len(nums)
        i = 0
        for r in range(n - k,2*n - k):
            idx_elem[i] = nums[r % n] 
            i += 1
        
        for i in range(n):
            nums[i] = idx_elem[i]
        


        