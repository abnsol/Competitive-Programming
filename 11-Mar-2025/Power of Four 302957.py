# Problem: Power of Four - https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and math.log(n)/math.log(2) % 2 == 0


        