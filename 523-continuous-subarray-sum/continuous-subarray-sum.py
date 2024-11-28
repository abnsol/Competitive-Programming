class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0 : -1}
        ttl = 0

        for i,n in enumerate(nums):
            ttl += n
            r = ttl % k
            if r not in remainder:
                remainder[r] = i
            elif i - remainder[r] > 1:
                return True 
            
        return False
'''
23 2 4 6 7
'''