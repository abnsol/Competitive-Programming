# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findBitString(self,n):
        if n == 1:
            return [0]
        
        prev = self.findBitString(n - 1)
        inverted = [i^1 for i in prev]
        ans = prev + [1] + inverted[::-1]

        return ans

    def findKthBit(self, n: int, k: int) -> str:
        bitString = self.findBitString(n)
        return str(bitString[k - 1])

        