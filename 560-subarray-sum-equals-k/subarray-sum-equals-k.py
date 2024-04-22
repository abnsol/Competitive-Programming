class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # variant of 974
        cnt = Counter({0 : 1})
        ans = ttl = 0

        for num in nums:
            ttl += num
            ans += cnt[ttl - k]  # is the ttl - k in cnt 
            cnt[ttl] += 1        # 
        
        return ans
            

         