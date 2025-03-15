# Problem: Find the Winner of the Circular Game - https://leetcode.com/problems/find-the-winner-of-the-circular-game/

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n,k):
            if n == 1:
                return 0
            
            return (helper(n - 1,k) + k) % n
        
        return helper(n,k) + 1