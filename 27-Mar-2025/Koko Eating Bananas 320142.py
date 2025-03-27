# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def validate(speed):
            hours = 0
            for pile in piles:
                if pile <= speed:
                    hours += 1
                else:
                    hours += ceil(pile/speed)

            return hours <= h
        
        l = 0
        r = sum(piles) + 1
        while r - l > 1:
            m = (r + l) // 2
            if validate(m):
                r = m
            else:
                l = m

        return r 