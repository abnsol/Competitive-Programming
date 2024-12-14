class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        vowelCnt = 0
        l = 0

        for r in range(k):
            if s[r] in vowels:
                vowelCnt += 1
        
        res = vowelCnt

        for r in range(k,len(s)):
            if s[r] in vowels:
                vowelCnt += 1
            
            if s[l] in vowels:
                vowelCnt -= 1

            l += 1
            
            res = max(res,vowelCnt)
        
        return res
            
        