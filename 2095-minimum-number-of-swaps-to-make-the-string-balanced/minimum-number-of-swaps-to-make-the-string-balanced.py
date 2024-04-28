class Solution:
    def minSwaps(self, s: str) -> int:
        # more of get the method
        ans = 0         # number of opened bracket that arent closed 
        for c in s:
            if c == "[":
                ans += 1
            elif ans:   # if ans is zero there are no opened bracket that arent closed
                ans -= 1
        
        return (ans + 1) // 2 # remember 1 swap closes(validates) 2 open brackets