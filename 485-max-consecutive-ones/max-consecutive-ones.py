class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxRes = l = 0 
        
        for r in range(len(nums)):
            if nums[r] == 0:
                l = r + 1
            else:
                maxRes = max(maxRes,r - l + 1)

        return maxRes
        