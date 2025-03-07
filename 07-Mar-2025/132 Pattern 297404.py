# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # mono decreasing 
        # keep min 
        stk = []   # tuple (num,minsofar)
        min_sofar = float("inf")
        for num in nums:
            while stk and stk[-1][0] <= num:
                stk.pop()
            
            if stk and stk[-1][1] < num < stk[-1][0]:
                return True
            
            stk.append([num,min_sofar])
            min_sofar = min(min_sofar,num)

        return False
        