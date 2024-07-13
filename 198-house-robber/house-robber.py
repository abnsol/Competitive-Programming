class Solution:
    def rob(self, nums: List[int]) -> int:
        prevrob = prevnorob = 0

        for i in nums:
            temp = max(prevrob,prevnorob)
            prevrob = prevnorob + i
            prevnorob = temp
        
        return max(prevrob,prevnorob)

        
        