# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])

        diags = defaultdict(list)
        for i in range(row):
            for j in range(col):
                diags[i + j].append(mat[i][j])
        
        ans = []
        for key in diags:
            if key % 2 == 0:
                ans += diags[key][::-1]
            else:
                ans += diags[key]

        return ans         
