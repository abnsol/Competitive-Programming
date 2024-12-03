class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        spaces = set(spaces)
        ans = []
        for idx,letter in enumerate(s):
            if idx in spaces:
                ans.append(" ")
                
            ans.append(letter)
        
        return "".join(ans)