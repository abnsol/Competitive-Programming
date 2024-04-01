class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        l,r = 0, len(piles) - 2
        max_coins = 0
        
        while l < r :
            max_coins += piles[r]
            l += 1
            r -= 2
        return max_coins


        