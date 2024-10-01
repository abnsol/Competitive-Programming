class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        while l < len(nums) and nums[l] != 0:
            l += 1
            r += 1

        while r < len(nums):
            while r < len(nums) and nums[r] == 0:
                r += 1
            
            if r < len(nums):
                nums[l],nums[r] = nums[r],nums[l]
                while l < len(nums) and nums[l] != 0:
                    l += 1
                r += 1
        
        return nums

'''
    1  3  0  0  12
          l     r 
'''