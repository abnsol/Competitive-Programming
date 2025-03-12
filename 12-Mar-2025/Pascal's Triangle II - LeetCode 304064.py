# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, n: int) -> List[int]:
        if n == 0:
            return [1]
        
        prev = self.getRow(n - 1)
        row = []
        for i in range(n//2 + 1):
            if i == 0:
                row.append(1)
            else:
                row.append(prev[i - 1] + prev[i])
        
        ans = []
        if n % 2 != 0:
            ans += row + row[::-1]   
        else:
            ans += row + list(reversed(row[:-1])) 
        
        return ans
        