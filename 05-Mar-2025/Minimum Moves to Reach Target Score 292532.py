# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0
        while target != 1:
            if target % 2 == 0 and maxDoubles:
                target //= 2
                maxDoubles -= 1
            elif not maxDoubles:
                ans += (target - 1)
                break
            else:
                target -= 1
            ans += 1
        return ans
        