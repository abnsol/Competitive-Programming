# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l ,r = -1, len(nums)

        while r - l > 1:
            m = (r + l) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m
        
        return l if nums[l] == target else -1
