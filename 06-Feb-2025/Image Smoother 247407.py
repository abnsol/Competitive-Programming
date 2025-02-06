# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row_len,col_len = len(img),len(img[0])
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        def inbound(i,j):
            return 0 <= i < row_len and 0 <= j < col_len
        
        ans = [[0]*col_len for _ in range(row_len)]
        for i in range(row_len):
            for j in range(col_len):
                num = 1
                ttl = img[i][j]
                for r,c in dirs:
                    nr = i + r
                    nc = j + c
                    if inbound(nr,nc):
                        ttl += img[nr][nc]
                        num += 1
                av = ttl//num
                ans[i][j] = av
        
        return ans


        