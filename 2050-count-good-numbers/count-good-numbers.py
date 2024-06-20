class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        m = n//2
        ans = 1    # identity place holder

        if n % 2 == 0:
            ans *= pow(5,m,mod)
            ans *= pow(4,m,mod)
            return ans % mod
        else:
            ans *= pow(5,m + 1,mod)
            ans *= pow(4,m,mod)
            return ans % mod

'''
10 

0 1 2 3 4 5 6 7 8 9 
5 4 5 4 5 4 5 4 5 4

evens = 2 4 6 8 0  total = 5
prime = 2 3 5 7  total = 4
'''
