# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
    
        closest = float('inf')
        for l in range(n):
            m = l + 1
            r = n - 1
            while m < r:
                total = nums[l] + nums[m] + nums[r]
                if target - total == 0:
                    return total

                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total > target:
                    r -= 1
                else:
                    m += 1

        return closest
