# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = -1
        ans = 1
        for i in range(time):
            if i % (n - 1) == 0:
                direction = -(direction)
            ans += direction
        return ans