class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdigit():
                stack.append(c)
            elif c[0] == "-" and c[1:].isdigit():
                stack.append(c)
            else:
                operand1 = str(stack.pop())
                operand2 = str(stack.pop())
                exp = operand2 + c + operand1
                val = int(eval(exp))
                stack.append(val)
        
        return int(stack[-1])