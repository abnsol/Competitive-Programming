# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countL = countR = ans = 0
        for i in s:
            if i == "L":
                countL += 1
            else:
                countR += 1
    
            if countR - countL == 0:
                countL = countR = 0
                ans += 1

        return ans