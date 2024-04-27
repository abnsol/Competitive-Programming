class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)           
            while len(stack) >= 2 and gcd(stack[-2],stack[-1]) > 1: 
                x = stack.pop()
                y = stack.pop()
                stack.append(x * y//gcd(y,x))                

        return stack      