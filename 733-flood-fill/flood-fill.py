class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dirs = [(0,1),(-1,0),(0,-1),(1,0)]
        val = image[sr][sc]
        visited = set()

        def inbound(i,j):
            return 0 <= i < len(image) and 0 <= j < len(image[0])

        def dfs(i,j):
            if (i,j) in visited or not inbound(i,j) or image[i][j] != val:
                return 
            
            image[i][j] = color
            visited.add((i,j))
            for r,c in dirs:
                dfs(i + r,j + c)
        
        dfs(sr,sc)
        return image