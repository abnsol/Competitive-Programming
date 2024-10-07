class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for letter in s:
            if stack and (stack[-1] + letter == 'AB' or stack[-1] + letter == 'CD'):
                stack.pop()
            else:
                stack.append(letter)
        
        return len(stack)