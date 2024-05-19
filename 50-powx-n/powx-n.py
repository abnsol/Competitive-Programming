class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x,abs(n))
        
        if n == 0:
            return 1
        
        if n == 1:
            return x
        
        if n & 1 == 1:
            res = self.myPow(x,n >> 1)
            return x * res * res
        else:
            res = self.myPow(x, n >> 1)
            return res * res
            