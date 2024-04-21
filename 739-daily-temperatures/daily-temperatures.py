class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # if temp less than the previous add to stack
        # when a greater temp comes pop and put it in the right position
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for idx, temp in enumerate(temperatures): # use enumerate!
            while stack and temp > stack[-1][0]:
                t , i  = stack.pop()
                ans[i] = idx - i      # number of less tempratures
            
            stack.append((temp,idx))
        
        return ans


            
            
