# Problem: Two Sum - https://leetcode.com/problems/two-sum/description

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i,x in enumerate(nums):
            y=target-x
            if y in d:
                return [d[y],i]
            d[x]=i
        return  []
        