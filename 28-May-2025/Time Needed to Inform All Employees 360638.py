# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = collections.defaultdict(list)
        self.res = 0
        for i, v in enumerate(manager):
            subordinates[v].append(i)
        
        def dfs(manager, time):
            self.res = max(self.res, time)
            for subordinate in subordinates[manager]:
                dfs(subordinate, time + informTime[manager])
        dfs(headID, 0)        
        return self.res