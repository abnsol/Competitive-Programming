# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0: return 0
        return self.trailingZeroes(n//5) + n//5

'''
1 2 6 24 120 720 
'''