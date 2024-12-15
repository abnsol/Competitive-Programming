class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        l = ttl = 0

        for r in range(n):
            ttl += nums[r]
            
            while ttl >= target:
                res = min(res,r - l + 1)
                ttl -= nums[l]
                l += 1
        
        if res == n + 1:
            return 0
        else:
            return res
        


'''
add => ttl 
check => >= target
    remove => l += 1
'''
        