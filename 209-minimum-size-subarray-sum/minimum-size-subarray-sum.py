class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        ttl = l = 0

        for r in range(n):
            ttl += nums[r]
            while l <= r and ttl >= target:
                res = min(res,r - l + 1)
                ttl -= nums[l]
                l += 1
            
        return 0 if res == n + 1 else res



'''

'''