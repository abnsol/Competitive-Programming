# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        A = []
        for row, limit in zip(grid, limits):
            A += nlargest(min(k, limit), row)
        return sum(nlargest(k, A))
        