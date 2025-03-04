# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        pos = float("-inf")
        ans = 0

        for s,e in points:
            if s > pos: 
                ans += 1 
                pos = e
            elif e < pos:
                pos = e
        
        return ans
            

            
        