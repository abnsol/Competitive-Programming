# Problem: Apply Operations to an Array - https://leetcode.com/problems/apply-operations-to-an-array/

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)
        while i < n - 1:
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
                i += 1
            i += 1
    
        i = 0
        while i < n:
            if nums[i] == 0:
                temp = i + 1
                while temp < n:
                    if nums[temp] > 0:
                        nums[i],nums[temp] = nums[temp],nums[i]
                        break
                    temp += 1
                
                if temp >= n:
                    return nums
            i += 1
        return nums

        