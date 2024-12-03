class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = ""
        l = 0
        for r in spaces:
            ans += (s[l:r] + " ")
            l = r

        ans += s[l:] 
        return ans