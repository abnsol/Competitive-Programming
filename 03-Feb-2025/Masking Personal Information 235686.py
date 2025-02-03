# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        ans = ""
        if "@" in s:
            splitted = s.split("@")
            ans = splitted[0][0].lower() + "*****" +  splitted[0][-1].lower() + "@" + splitted[1].lower()
        else:
            p = ""
            separator = "()-+ "
            for i in s:
                if i not in separator:
                    p += i
            
            ans += ("***-***-" + p[-4:])
            if len(p) > 10:
                ans = "+" + "*"*(len(p) - 10) + "-" + ans

        return ans 



            
            
            