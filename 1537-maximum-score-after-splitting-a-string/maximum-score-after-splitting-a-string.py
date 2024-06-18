class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left = [0] * (n)
        right = [0] * (n)
        total = [0] * (n)
        z = o = 0

        for i in range(n):
            if s[i] == '0':
                z += 1
            
            if s[n - (i + 1)] == '1':
                o += 1
            
            left[i] = z
            right[n - (i + 1)] = o
        
        for i in range(n - 1):
            total[i] = left[i] + right[i + 1]
        
        return max(total)
        


