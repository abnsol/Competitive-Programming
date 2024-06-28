class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def wheel_division(n):
            while n % 2 == 0:
                ans.add(2)
                n //= 2

            d = 3
            while d * d <= n:
                while n%d == 0:
                    ans.add(d)
                    n//=d
                d += 1

            if n > 1:
                ans.add(n)

        ans = set()
        for n in nums:
            wheel_division(n)
        return len(ans) 
        