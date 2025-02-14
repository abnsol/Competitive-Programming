# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        
        cntS1 = Counter(s1)
        cntS2 = Counter(s2[:m])
        # print(cntS2)
        if cntS2 == cntS1: return True

        for r in range(m,n):
            cntS2[s2[r]] += 1
            cntS2[s2[r - m]] -= 1
            if cntS2[s2[r - m]] == 0:
                del cntS2[s2[r - m]]

            if cntS2 == cntS1: return True
        
        return False




        