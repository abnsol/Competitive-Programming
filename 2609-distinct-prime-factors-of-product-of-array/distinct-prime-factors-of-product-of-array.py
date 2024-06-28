class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        pro = 1
        for n in nums:
            pro *= n

        def wheel_division(n):
            d = 2
            while d * d < n:
                while n%d == 0:
                    ans.add(d)
                    n//=d
                d += 1

            if n > 1:
                ans.add(n)

        ans = set()
        wheel_division(pro)
        return len(ans) 
        