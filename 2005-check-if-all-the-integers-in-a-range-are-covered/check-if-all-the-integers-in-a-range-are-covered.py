class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        joined = []
        for i in ranges:
            start = i[0]
            end = i[1]
            joined += list(range(start,end+1))
        
        for num in range(left,right + 1):
            if num not in joined:
                return False
        return True
            


        