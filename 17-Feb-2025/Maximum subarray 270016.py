# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ps = 0
        ans = float('-inf')
        for num in nums:
            ps += num
            if ps < 0:
                ans = max(ans,ps)
                ps = 0
            else:
                ans = max(ans,ps)
        
        return ans

        