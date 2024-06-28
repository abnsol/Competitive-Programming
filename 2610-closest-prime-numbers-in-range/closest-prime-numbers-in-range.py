class Solution:
    def sievetillroot(self,n):
        isprime = [True for _ in range(n + 1)]
        isprime[0] = isprime[1] = False
        i = 2
        while i * i <= n:
            if isprime[i]:
                j = i * i 
                while j <= n:
                    isprime[j] = False
                    j += i
            i += 1
        return isprime

    def closestPrimes(self, left: int, right: int) -> List[int]:
        prime = self.sievetillroot(right)

        l = left 
        while l <= right and not prime[l]:
            l += 1
        if l > right:
            return [-1,-1]
        
        r = l + 1
        _min = float('inf')
        _range = []
        while r <= right:
            if prime[r]:
                if r - l < _min:
                    _range = [l,r]
                    _min = r - l 
                l = r
            r += 1
        
        if _range:
            return _range
        return [-1,-1]





        