class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ']':
                sub = ''
                while stack[-1] != '[':
                    sub = stack.pop() + sub 
                stack.pop()
                
                n = ''
                while stack and stack[-1].isdigit():
                    n = stack.pop() + n
                stack.append(sub * int(n))

            else:
                stack.append(s[i])
        
        return ''.join(stack)



