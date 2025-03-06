# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)

        for idx,val in enumerate(temperatures):
            while stk and stk[-1][0] < val:
                v, i = stk.pop()
                ans[i] = idx - i
            
            stk.append([val,idx])

        return ans
            