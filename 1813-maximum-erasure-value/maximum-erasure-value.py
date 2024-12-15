class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt = Counter()
        l = res = ttl = 0

        for r in range(len(nums)):
            ttl += nums[r]
            cnt[nums[r]] += 1

            while cnt[nums[r]] > 1:
                ttl -= nums[l]
                cnt[nums[l]] -= 1
                l += 1
            
            res = max(res,ttl)
        
        return res
                

        