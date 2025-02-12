# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort(key = lambda a: a * 10,reverse = True)
        if nums_str[0] == "0":
            return "0"
        
        return "".join(nums_str)