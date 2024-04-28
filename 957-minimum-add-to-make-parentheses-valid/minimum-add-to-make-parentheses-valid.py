class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        valid = "()"
        stack = []

        for c in s:
            if not stack: 
                stack.append(c)
                continue
            
            if stack[-1] + c in valid:
                stack.pop()
            else:
                stack.append(c)

        return len(stack)
                

