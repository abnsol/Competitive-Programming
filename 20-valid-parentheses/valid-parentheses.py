class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid = "()[]{}"

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if stack and stack[-1] + char in valid:
                    stack.pop()
                else:
                    return False
        
        if not stack: return True
        return False
