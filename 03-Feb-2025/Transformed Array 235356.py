# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            num = nums[i]
            idx = (i + num) % n
            result[i] = nums[idx]
            
        return result

            


        