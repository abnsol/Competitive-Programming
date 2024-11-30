class Solution:
    def removeStars(self, s: str) -> str:
        stk = []
        for char in s:
            if char == "*":
                stk.pop()
            else:
                stk.append(char)
        
        return "".join(stk)
        

'''
when u get a star just pop
'''