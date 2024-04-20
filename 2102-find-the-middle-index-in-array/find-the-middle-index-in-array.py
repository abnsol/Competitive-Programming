class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix_sum = 0

        for i in range(len(nums)):
            suffix_sum = total - nums[i] - prefix_sum
            if prefix_sum == suffix_sum:
                return i
            prefix_sum += nums[i]
        
        return -1