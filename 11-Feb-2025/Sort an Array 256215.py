# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val, max_val = abs(min(nums)),max(nums)
        cnt = [0] * (max_val + min_val + 1)
        
        for i in nums:
            cnt[i + min_val] += 1

        target = 0
        for i,v in enumerate(cnt):
            for j in range(v):
                nums[target] = i - min_val
                target += 1

        
        return nums
        