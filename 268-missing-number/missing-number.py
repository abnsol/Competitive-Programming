class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i] and nums[i] < len(nums):
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]

        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)