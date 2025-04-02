# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n = len(houses)
        k = len(heaters)
        
        houses.sort()
        heaters.sort()

        def validate(valid_range):
            i = 0
            for house in houses:
                while i < k and abs(house - heaters[i]) > valid_range:
                    i += 1
                
                if i == k:
                    return False

            return True           

        l, r = -1, max(heaters[-1],houses[-1]) + 1
        while r > l + 1:
            m = (r + l) // 2
            if validate(m):
                r = m
            else:
                l = m
        
        return r

        