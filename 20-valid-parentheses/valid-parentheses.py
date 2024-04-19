class Solution:
    def isValid(self, s: str) -> bool:
        Brackets = {"()","{}","[]"} # Valid Pairs
        stack = []

        for char in s:
            if char in "({[":  # open Brackets
                stack.append(char)
            # if our stack is empty or last open bracket in our stack + the close bracket doesnt match
            elif not stack or stack.pop() + char not in Brackets: 
                return False
                
        # so when we finish stack must be empty = false 
        return not stack 
