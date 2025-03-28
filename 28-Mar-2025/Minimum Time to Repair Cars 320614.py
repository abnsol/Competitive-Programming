# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def validate(time):
            repaired = 0
            for rank in ranks:
                repaired += int((time//rank) ** 0.5)
            
            return repaired >= cars
        
        l, r = 0, max(ranks) * (cars ** 2)
        while r > l + 1:
            m = (l + r) // 2
            if validate(m):
                r = m
            else:
                l = m

        return r 