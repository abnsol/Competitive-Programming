class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for r in range(len(nums)):
            l = r - 1
            key = nums[r]
            while nums[l] == 0 and l >= 0:
                nums[l+1] = nums[l]
                l -= 1
            nums[l+1] = key


        