# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        stkDigit = []
        n = len(s)
        i = 0

        while i < n:
            if s[i].isdigit():
                num = []
                while s[i].isdigit():
                    num.append(s[i])
                    i += 1
                stkDigit.append(int("".join(num)))
            
            if s[i] == "]":
                strings = []
                while stk[-1] != "[":
                    strings += [stk.pop()]
                stk.pop()
                stk.append(stkDigit.pop() * "".join(strings[::-1]))
            else:
                stk.append(s[i])
            
            i += 1
    
        return "".join(stk)

        