# Problem: Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = -1, n
        while l + 1 < r:
            m = (l + r) // 2
            if nums[-1] < nums[m]:
                l = m
            else:
                r = m
        
        return nums[r] if r != n else nums[0]
        