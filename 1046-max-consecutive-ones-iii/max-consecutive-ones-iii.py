class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = count = maxLength = 0
        n = len(nums)
        for r in range(n):
            if nums[r] == 0:
                count += 1
            
            while count > k:
                if nums[l] == 0:
                    count -= 1
                
                l += 1
            
            maxLength = max(maxLength,r - l + 1)
        
        return maxLength
        