class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""

        ans = strs[0]
        n = len(strs)
        for i in range(1,n):
            prefix = ""
            j = k = 0
            while j < len(ans) and k < len(strs[i]):
                if ans[j] == strs[i][k]:
                    prefix += ans[j]
                    j += 1
                    k += 1
                else:
                    break

            ans = prefix
        
        return ans




        