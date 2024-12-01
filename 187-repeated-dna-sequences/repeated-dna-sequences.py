class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        subString = set()
        l = 0
        ans = set()
        for r in range(10,n + 1):
            subStr = s[l:r]
            if subStr in subString:
                ans.add(subStr)
            
            subString.add(subStr)
            l += 1
        
        return list(ans)
                

        
        