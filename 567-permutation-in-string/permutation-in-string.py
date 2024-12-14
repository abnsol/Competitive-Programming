class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)
        n = len(s2)
        l = 0

        if m > n: return False

        cnt = Counter(s1)
        cntS2 = {}

        for _ in range(m):
            cntS2[s2[_]] = cntS2.get(s2[_],0) + 1
        
        if cntS2 == cnt: return True

        for r in range(m,n):
            cntS2[s2[r]] = cntS2.get(s2[r],0) + 1
            cntS2[s2[l]] -= 1
            if not cntS2[s2[l]]: del cntS2[s2[l]]
            l += 1
            if cntS2 == cnt: return True
        
        return False





'''
s1.len > s2.len return false
k = s1.len
fixed Sw approach

'''

        