# Problem: Palindrome Number  - https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        total=0
        while x>0:
            total = (total * 10) + x % 10
            x//=10
        return total==y