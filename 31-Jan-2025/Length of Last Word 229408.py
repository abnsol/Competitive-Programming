# Problem: Length of Last Word - https://leetcode.com/problems/length-of-last-word/description/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s) - 1
        while n >= 0 and s[n] == " ":
              n -= 1
 
        end = n
        while n >= 0:
            if s[n] == " ":
                break 
            n -= 1
        
        return end - n

        