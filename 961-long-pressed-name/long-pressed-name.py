class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = j = 0
        nameLen = len(name)
        typedLen = len(typed)
        while i < nameLen and j < typedLen:
            if name[i] != typed[j]:
                return False
                
            else:
                if i + 1 < nameLen and name[i] == name[i + 1]:
                    i += 1
                    j += 1
                    continue

                while j < typedLen and name[i] == typed[j]:
                    j += 1
                i += 1
        
        if i == nameLen and j == typedLen:
            return True
        return False
