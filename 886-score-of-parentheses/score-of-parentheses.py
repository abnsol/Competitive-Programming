class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = 0
        stk = [] 

        for i in s:
            if i == "(":
                stk.append(0)
            else:
                # print('before',stk)
                val = stk.pop()
                # print('val',val)
                if stk and val == 0:
                    # print('stk',stk[-1])
                    stk[-1] += 2 * (val + 1)
                elif stk and val != 0:
                    stk[-1] += 2 * (val)
                elif not stk and val == 0:
                    res += (val + 1)
                elif not stk and val != 0:
                    res += val
                # print('after',stk)

        return res


'''
"(()(()))"
( 6

'''