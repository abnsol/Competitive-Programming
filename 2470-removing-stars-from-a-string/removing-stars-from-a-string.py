class Solution:
    def removeStars(self, s: str) -> str:
        stk = []

        for letter in s:
            if letter == "*":
                stk.pop()
            else:
                stk.append(letter)
        
        return "".join(stk)

        