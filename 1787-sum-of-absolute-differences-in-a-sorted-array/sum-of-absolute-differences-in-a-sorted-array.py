class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # main intuition is we have to find the sum 
        # before the element and after the element
        # independently and dont forget to multiply the number
        # to the amount of number before and after it
        n = len(nums)
        prefix = [0]
        suffix = [0]

        for i in range(n - 1):
            prefix.append(prefix[i] + nums[i])
            suffix.append(suffix[i] + nums[n - 1 - i])
        
        suffix.reverse()
        ans = []
        for i in range(n):
            res = (nums[i] * i) - prefix[i] \
            + abs(nums[i] * (n - 1 - i) - suffix[i])
            ans.append(res)
        
        return ans



'''
[1,4,6,8,10]
[0,1,5,11,19]
[28,24,18,10,0]
(1 * 0) - 0  + |1 * (5 - 0 - 1) - 28|  = 24
(4 * 1) - 1 + |4 * (5 - 1 - 1) - 24| = 3 + 12 = 15
(6 * 2) - 5 + |6 * (5 - 2 - 1) - 18| = 7 + 6 = 13
'''