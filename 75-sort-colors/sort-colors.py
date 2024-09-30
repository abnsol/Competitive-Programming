class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = m = 0
        r = len(nums) - 1

        while l < len(nums) and nums[l] == 0:
            l += 1
            m += 1
        
        while r > -1 and nums[r] == 2:
            r -= 1

        while m <= r: 
            if nums[m] == 0:
                nums[m],nums[l] = nums[l], nums[m]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[r],nums[m] = nums[m],nums[r]
                r -= 1
            else:
                m += 1
            
        return nums