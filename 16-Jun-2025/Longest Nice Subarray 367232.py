# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r = 0, 0
        mx = 1
        bits = 0
        while r < len(nums):
            if (bits | nums[r]) == bits + nums[r]:
                bits |= nums[r]
                r += 1
            else:
                bits &= ~nums[l]
                l += 1
            mx = max(mx, r - l)
        return mx