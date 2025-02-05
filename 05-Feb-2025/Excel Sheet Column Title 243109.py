# Problem: Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/description/?envType=problem-list-v2&envId=string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        place = 0
        ans = []
        while columnNumber > 0:
            columnNumber -= 1
            mod = columnNumber % 26
            ans.append(chr(mod + 65))
            columnNumber //= 26
        
        return "".join(reversed(ans)) 
                    