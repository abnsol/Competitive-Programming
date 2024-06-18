class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # so the goal is to find all subarrrays whose sum <= goal and sum <= goal - 1 so the difference between them will give us the total subarrays whose sum = goal

        def helper(nums,goal):
            # use sliding window to find sum <= goal
            if goal < 0: return 0

            l = total = totalSub = 0
            for r in range(len(nums)):
                total += nums[r]
                while l < r and total > goal:
                    total -= nums[l]
                    l += 1
                
                if total <= goal:
                    totalSub += r - l + 1
            
            return totalSub
        
        first = helper(nums,goal)
        second = helper(nums,goal - 1)

        return first - second
