# Problem: Separate the Digits in an Array - https://leetcode.com/problems/separate-the-digits-in-an-array/description/

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def digits(num):
            ans = []
            while num > 0:
                ans.append(num % 10)
                num //= 10
            
            ans.reverse()
            return ans

        ans = []
        for num in nums:
            ans += digits(num)
        
        return ans

        