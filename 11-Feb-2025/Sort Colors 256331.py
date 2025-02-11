# Problem: Sort Colors - https://leetcode.com/problems/sort-colors/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums),max(nums)
        hashmap = {i:0 for i in range(min_val,max_val + 1)}
        
        for i in nums:
            hashmap[i] += 1
            
        ans = []
        for i in hashmap:
            if hashmap[i] > 0:
                ans += [i] * hashmap[i]
        
        return ans
        