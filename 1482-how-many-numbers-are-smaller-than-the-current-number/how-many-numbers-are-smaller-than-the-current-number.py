class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        for i in nums:
            less = 0
            for j in nums:
                if j < i:
                    less += 1
            
            ans.append(less)
        
        return ans
