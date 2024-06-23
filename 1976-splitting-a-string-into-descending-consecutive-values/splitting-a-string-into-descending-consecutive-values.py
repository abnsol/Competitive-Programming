class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(idx,prev):
            if idx == len(s):
                return True
            
            for j in range(idx,len(s)):
                val = int(s[idx:j + 1])                # next cut and prev
                if val + 1 == prev and dfs(j + 1,val): # continue depth if 
                    return True
            return False
        
        for i in range(len(s) - 1):
            val = int(s[:i + 1])                       # first cut | digit
            if dfs(i + 1,val): return True
        return False



''' 
 
'''