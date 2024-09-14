class Solution:
    def findComplement(self, num: int) -> int:
        n = int.bit_length(num)
        for i in range(n):
            num ^= (1 << i)
        
        return num
