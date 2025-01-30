# Problem: Goal Parser Interpretation - https://leetcode.com/problems/goal-parser-interpretation/description/

class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        for i in range(len(command)):
            if command[i] == "G":
                ans += "G"
            elif command[i] == "(":
                if command[i + 1] == ")":
                    ans += "o"
                else:
                    ans += "al"
            else:
                continue
        return ans
        