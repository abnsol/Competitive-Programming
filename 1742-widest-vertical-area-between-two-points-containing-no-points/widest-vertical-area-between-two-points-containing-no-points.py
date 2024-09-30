class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[0])
        maxWidth = float('-inf')

        for i in range(1,len(points)):
            maxWidth = max(points[i][0] - points[i - 1][0],maxWidth)
        
        return maxWidth


# [1,0][1,4][3,1][5,3][8,8][9,0]

# max = 2
#       2
#       3
#       1