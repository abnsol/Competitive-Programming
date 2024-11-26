class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            nums[i] = acc
        
        return nums
        