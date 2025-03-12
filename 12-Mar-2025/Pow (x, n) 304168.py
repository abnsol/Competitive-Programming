# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def power(self,x,n):
        if n == 0: return 1
        if n == 1 or n == -1:
            return x
        
        ans = self.power(x,n//2)
        if n % 2 == 0:
            return ans * ans
        else:
            return  ans * ans * x 

    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            return self.power(x,n)
        else:
            return 1/self.power(x,abs(n))
    
