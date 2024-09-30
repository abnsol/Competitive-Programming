class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        newPoints = []
        for x,y in points:
            distance = x**2 + y**2
            newPoints.append([[x,y],[distance]])
        
        newPoints.sort(key = lambda x : x[1])
        return [newPoints[i][0] for i in range(k)]