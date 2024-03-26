class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        positive = 1
        for i in range(len(nums)):
            if nums[i] < positive:
                continue
            elif nums[i] == positive:
                positive += 1
            else:
                return  positive
        return positive
