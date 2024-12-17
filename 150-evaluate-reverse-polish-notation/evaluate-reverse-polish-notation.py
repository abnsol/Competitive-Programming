class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = {"+","-","*","/"}

        for char in tokens:
            if char in operators:
                poppedF = stk.pop()
                poppedS = stk.pop()
                res = str(int(eval(poppedS + char + poppedF)))
                stk.append(res)
            else:
                stk.append(char)
        
        return int(stk[0])
'''
2 1
3 3 
9
secondPopped firstPopped

4 13 5

stk = []
'''