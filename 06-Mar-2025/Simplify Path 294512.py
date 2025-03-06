# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted_path = path.split("/")
        stk = []

        for char in splitted_path:
            if stk and char == "..":
                stk.pop()
            elif char != ".." and char != "." and char != "":
                stk.append(char)
        
        return "/" + "/".join(stk)


'''
/ 
["...","a","..","b","c","..","d","."]
/
/
'''