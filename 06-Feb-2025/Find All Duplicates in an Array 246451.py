# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            idx = abs(i) - 1
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] *= -1
        return ans
            
        