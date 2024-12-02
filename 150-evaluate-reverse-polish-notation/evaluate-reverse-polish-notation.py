class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {'+','-','*','/'}
        for token in tokens:
            if token in ops:
                op1 = stk.pop()
                op2 = stk.pop()
                exp = str(op2) + token + str(op1)
                stk.append(int(eval(exp)))
                continue
            
            stk.append(token)
        
        return int(stk[0])


'''
10 6 -131 /
'''