class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] > 0 or nums[right] < 0:
                return -1
            if abs(nums[left]) > abs(nums[right]):
                left += 1
            elif abs(nums[left]) < abs(nums[right]):
                right -= 1
            else:
                return nums[right]
        
        return -1
