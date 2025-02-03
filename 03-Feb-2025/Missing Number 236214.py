# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sett = set(nums)
        n = len(nums)
        for i in range(n):
            if i not in sett:
                return i
        return n 
        