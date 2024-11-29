class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ttl = 0
        res = nums[0]

        for num in nums:
            ttl += num
            if ttl < 0:
                res = max(res,ttl)
                ttl = 0
            else:
                res = max(res,ttl)
        
        return res


'''
-2 1 -2 4 3 5 6 1 5
5 9 8 15 23  

ttl = 0
res = nums[0]
max(res,ttl)
'''