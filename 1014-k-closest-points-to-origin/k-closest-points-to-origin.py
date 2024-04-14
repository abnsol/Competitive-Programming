class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []  # include tuples (dis,points)
        for x , y in points:
            dis = x**2 + y**2
            closest.append((dis,[x,y]))
        
        closest.sort()
        ans = []
        for i in range(k):
            ans.append(closest[i][1])
        return ans