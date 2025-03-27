# Problem: First Bad Version - https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n + 1
        while l < r - 1:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m
        
        return r 
        