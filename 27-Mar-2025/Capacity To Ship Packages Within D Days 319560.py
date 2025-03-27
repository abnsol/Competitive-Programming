# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    
        def validate(capacity):
            daysNeeded = 1
            load = 0
            for weight in weights:
                load += weight

                if load > capacity:
                    daysNeeded += 1
                    load = weight

                    if daysNeeded > days:
                        return False
                
            return True
        
        l = max(weights)
        r = sum(weights)
        while l < r:
            m = (l + r) // 2 
            ans = validate(m)
            if validate(m):
                r = m
            else:
                l = m + 1
        
        return r
