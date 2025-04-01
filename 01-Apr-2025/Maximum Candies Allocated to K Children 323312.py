# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        def validate(m):
            child = k

            for candy in candies:
                child -= candy // m

                if child <= 0:
                    return True
            
            return False
        
        l, r = 0, max(candies) + 1
        while r > l + 1:
            m = (l + r) // 2
            if validate(m):
                l = m
            else:
                r = m
        
        return l