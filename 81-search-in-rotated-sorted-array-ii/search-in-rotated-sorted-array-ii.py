class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left , right = 0, len(nums) - 1
        while right > left and nums[left] == nums[right]:
            left += 1

        while right - left > 1:
            mid = left + (right - left)//2

            if nums[mid] == target:
                return True
            
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return True
        return False if nums[right] != target else True