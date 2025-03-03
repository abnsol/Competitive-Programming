# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        rangeUpdate = [0] * n
        for s,e in requests:
            rangeUpdate[s] += 1
            if e < n - 1: rangeUpdate[e + 1] -= 1
        
        prefix_range_update = list(accumulate(rangeUpdate))
        prefix_range_update.sort()
        nums.sort()
        ans = 0
        for i in range(n - 1,-1,-1):
            ans += (nums[i] * prefix_range_update[i])
        
        return ans % ((10**9) + 7)
