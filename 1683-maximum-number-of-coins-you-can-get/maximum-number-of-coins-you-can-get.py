class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        ans = l = 0
        r = len(piles) - 2

        while l < r:
            ans += piles[r]
            l += 1
            r -= 2
        
        return ans

        
