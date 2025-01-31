class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        n = len(goal)
        for i in range(n):
            temp = ""
            count = 0
            j = i
            while count < n:
                temp += goal[j % n]
                count += 1
                j += 1
            if temp == s:
                return True
        
        return False


                
        