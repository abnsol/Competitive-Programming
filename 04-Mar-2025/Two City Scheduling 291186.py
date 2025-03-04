# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda a:a[0] - a[1])
        n = len(costs)
        ans = 0
        for i in range(n):
            if i < n//2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]
       

        return ans

