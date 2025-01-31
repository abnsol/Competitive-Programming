class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return False if (len(goal) != len(s)) else goal in s + s


                
        