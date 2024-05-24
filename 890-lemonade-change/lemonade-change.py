class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        countbill = Counter();
        for i in bills:
            if i == 5:
                countbill[5] += 1
            elif i == 10:
                if countbill[5] == 0:return False
                countbill[5] -= 1
                countbill[10] += 1
            else:
                if countbill[10] == 0 and countbill[5] < 3: return False
                elif countbill[10] > 0 and countbill[5] == 0: return False
                elif countbill[10] == 0 and countbill[5] >= 3:
                    countbill[5] -= 3
                    countbill[20] += 1
                else:
                    countbill[10] -= 1
                    countbill[5] -= 1
                    countbill[20] += 1
        
        return True
            