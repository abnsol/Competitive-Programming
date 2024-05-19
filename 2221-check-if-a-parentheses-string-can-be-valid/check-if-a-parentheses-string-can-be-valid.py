class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        strlen = len(s)

        if strlen % 2 != 0:
            return False

        balance = 0
        for index in range(strlen):
            if s[index] == '(' or locked[index] == '0':
                balance += 1
            elif balance:
                balance -= 1
            else:
                return False
      
        balance = 0
        for index in range(strlen - 1, -1, -1):
            if s[index] == ')' or locked[index] == '0':
                balance += 1
            elif balance:
                balance -= 1
            else:
                return False
    
        return True