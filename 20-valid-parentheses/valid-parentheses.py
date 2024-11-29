class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        valids = "()[]{}"

        for bracket in s:
            if bracket in "([{":
                stk.append(bracket)
            else:
                if stk:
                    if stk.pop() + bracket not in valids:
                        return False
                else:
                    return False
        
        return True if not stk else False
                

        