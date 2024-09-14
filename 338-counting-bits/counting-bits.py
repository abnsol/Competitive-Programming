class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        
        for num in range(n + 1):
            ans.append(int.bit_count(num))

        return ans