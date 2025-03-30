# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(gap):
            prev = position[0]
            placed = 1
            
            for i in range(1,len(position)):
                cur = position[i]

                if cur - prev >= gap:
                    placed += 1
                    prev = cur
                
                if placed == m:
                    return True

            return False    

        l, r = 0, position[-1] + 1
        ans = 0

        while r > l + 1:
            mid = (l + r) // 2
            if check(mid):
                # ans = mid
                l = mid 
            else:  
                r = mid 

        return l