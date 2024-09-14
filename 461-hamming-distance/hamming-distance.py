class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return int.bit_count(x ^ y)