# Problem: Sum of Digits of String After Convert - https://leetcode.com/problems/sum-of-digits-of-string-after-convert/description/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ""
        for i in s:
            num = ord(i) - 96
            string += str(num)

        for i in range(k):
            ans = 0
            for i in string:
                ans += int(i)
            
            string = str(ans)
        
        return int(string)

        

        