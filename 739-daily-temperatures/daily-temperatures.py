class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stk = [] # temp,idx
        ans = [0] * n
        for idx,temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                poppedTemp,poppedIdx = stk.pop()
                ans[poppedIdx] = idx - poppedIdx
            
            stk.append([temp,idx])

        return ans

        