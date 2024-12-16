class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = m = 0
        r = n - 1

        while m <= r:
            if nums[m] == 0:
                nums[l],nums[m] = nums[m],nums[l]
                l += 1
                m += 1
            elif nums[m] == 2:
                nums[m],nums[r] = nums[r], nums[m]
                r -= 1
            else:
                m += 1
           


        