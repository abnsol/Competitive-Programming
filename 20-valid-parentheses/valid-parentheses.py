class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        valid = ["()","[]","{}"]

        for par in s:
            if par in "])}":
                if stk and stk[-1] + par in valid:
                    stk.pop()
                else:
                    return False
            else:
                stk.append(par)
        
        return False if stk else True

'''
close and open doesnt match
every open must be closed at the end
'''