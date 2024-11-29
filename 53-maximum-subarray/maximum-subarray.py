class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ttl = 0
        res = nums[0]

        for num in nums:
            ttl += num
            res = max(res,ttl)
            if ttl < 0:
                ttl = 0
        
        return res


'''
-2 1 -2 4 3 5 6 1 5
5 9 8 15 23  

ttl = 0
res = nums[0]
max(res,ttl)
'''