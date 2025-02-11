# Problem: Maximum Number of Coins You Can Get - https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        left = 0
        right = len(piles) - 2
        coins = 0
        while left < right:
            coins += piles[right]
            right -= 2
            left += 1
        return coins


        