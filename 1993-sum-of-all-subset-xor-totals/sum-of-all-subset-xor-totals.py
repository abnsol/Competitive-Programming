class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def gensubset(i,total):
            if i == len(nums):
                return total
            
            return gensubset(i + 1, total ^ nums[i]) + gensubset(i + 1, total)
        
        return gensubset(0,0)