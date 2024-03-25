class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
        
        return [nums[i] for i in range(len(nums)) if nums[i] != i + 1]