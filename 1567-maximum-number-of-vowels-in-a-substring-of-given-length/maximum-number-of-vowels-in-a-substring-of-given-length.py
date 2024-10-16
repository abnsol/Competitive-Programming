class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a','e','i','o','u'}
        count = r = maxLength = 0
        n = len(s)

        for _ in range(k):
            if s[_] in vowels:
                count += 1
            
            r += 1
        
        maxLength = count

        for i in range(r,n):
            if s[i - k] in vowels:
                count -= 1
            if s[i] in vowels:
                count += 1
            
            maxLength = max(maxLength,count)
        
        return maxLength
