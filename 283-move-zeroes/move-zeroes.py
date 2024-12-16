class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        n = len(nums)
        while l < n and nums[l] != 0:
            l += 1
        
        for r in range(l,n):
            if nums[r] == 0:
                continue
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        
    


"""
1 0 0 3 12
"""