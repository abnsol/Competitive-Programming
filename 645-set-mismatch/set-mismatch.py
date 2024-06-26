class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while i != nums[i] - 1 and nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1],nums[i] = nums[i],nums[nums[i] - 1]

        for i in range(n):
            if i + 1 != nums[i]:
                return [nums[i],i + 1]