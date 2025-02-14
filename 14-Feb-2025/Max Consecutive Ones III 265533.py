# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = l = 0

        for r in range(n):
            if nums[r] == 0:
                k -= 1
            
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1

            ans = max(ans,r - l + 1)

        return ans    
        