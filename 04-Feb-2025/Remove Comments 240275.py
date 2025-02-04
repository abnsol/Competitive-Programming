# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = ""
        joinedSrc = "~".join(source)
        n = len(joinedSrc)
        i = 0
        while i < n:
            if i < n - 1 and (joinedSrc[i] == "/" and joinedSrc[i + 1] == "*"): 
                i += 2
                while joinedSrc[i] + joinedSrc[i + 1] != "*/":
                    i += 1
                else: 
                    i += 2
            elif i < n - 1 and (joinedSrc[i] == "/" and joinedSrc[i + 1] == "/"):
                while i < n and joinedSrc[i] != "~":
                    i += 1
            else:
                res += joinedSrc[i]
                i += 1

        splitted = res.split("~")
        ans = []
        for i in splitted:
            if len(i) != 0:
                ans.append(i)
        
        return ans
            
        