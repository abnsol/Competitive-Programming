class Solution:
    def minInsertions(self, s: str) -> int:
        insertion = balance = 0
        i, n = 0, len(s)
        
        while i < n:
            if s[i] == '(':
                balance += 1
            else:
                if i < n - 1 and s[i + 1] == ')':
                    i += 1
                else:
                    insertion += 1
                
                if balance == 0:
                    insertion += 1
                else:
                    balance -= 1
            i += 1
        
        insertion += (balance * 2)
        return insertion