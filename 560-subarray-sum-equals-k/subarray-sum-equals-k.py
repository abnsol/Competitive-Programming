class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter({0:1})
        res = 0
        ttl = 0

        for num in nums:
            ttl += num
            res += cnt[ttl - k]
            cnt[ttl] += 1
        
        return res



'''
[0,1,2,3]
hashmap = {}
2 - x = k
x = 2 - k
'''