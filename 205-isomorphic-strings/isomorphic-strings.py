class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        for i in range(len(s)):
            if s[i] not in maps:
                maps[s[i]] = t[i]
                continue
            if maps[s[i]] != t[i]:
                return False
        
        maps1 = {}
        for i in range(len(s)):
            if t[i] not in maps1:
                maps1[t[i]] = s[i]
                continue
            if maps1[t[i]] != s[i]:
                return False
        return True
        

