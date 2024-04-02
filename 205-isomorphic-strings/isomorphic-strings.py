class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST ,mapTS = {} , {}
        for c, d  in zip(s,t):
            if ((c in mapST and  mapST[c] != d) or (d in mapTS and mapTS[d] != c)):
                return False
            mapST[c] = d
            mapTS[d] = c
        return True