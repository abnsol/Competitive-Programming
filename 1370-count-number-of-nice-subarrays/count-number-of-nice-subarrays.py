class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = ttl = res = 0
        n = len(nums)

        for r in range(n):
            if nums[r] % 2 == 1:
                k -= 1
                ttl = 0
            
            while k == 0:
                ttl += 1
                if nums[l] % 2 == 1:
                    k += 1
                l += 1
            
            res += ttl
        
        return res
        