# Problem: Check if All the Integers in a Range Are Covered - https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/description/

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        joined = []
        for s,e in ranges:
            joined += list(range(s,e + 1))
        
        for num in range(left,right + 1):
            if num not in joined:
                return False
        return True
            


        