# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0 
        r = c ** 0.5 // 1
        while l <= r:
            pro = l ** 2 + r ** 2
            if pro == c:
                return True
            elif pro > c:
                r -= 1
            else:
                l += 1
        
        return False
            


        