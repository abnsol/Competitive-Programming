# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        minimum = maximum = ttl = 0
        ans = float("-inf")  
        for num in nums:
            ttl += num
            ans = max(ans,ttl - minimum,maximum - ttl)
            minimum = min(ttl,minimum)
            maximum = max(ttl,maximum)
        
        return ans