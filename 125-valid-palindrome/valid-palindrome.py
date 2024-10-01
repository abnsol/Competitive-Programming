class Solution:
    def isPalindrome(self, s: str) -> bool:
        l ,r = 0, len(s) - 1

        while l < r:
            while (not s[l].isalnum()) and l < r:
                l += 1
            while (not s[r].isalnum()) and l < r:
                r -= 1
            
            if l > r:
                return False
            
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

'''
Two pointers approach

intialize my pointers
while left pointer lessthan right pointer
    check alphanumeric or not
        not: increase pointer accordingly
        is: check if left and right are the same (must be lower)
            not return false
            if increase accly

return true passed all the conditions
'''