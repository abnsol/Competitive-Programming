class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        operations = 0

        while left < right:
            temp = nums[right] + nums[left]
            if temp == k:
                operations += 1
                left += 1
                right -= 1
            elif temp > k:
                right -= 1
            else:
                left += 1
    
        return operations 

