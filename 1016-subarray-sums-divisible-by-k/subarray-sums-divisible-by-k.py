class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ttl = res = 0
        rem_to_cnt = Counter({0 : 1})

        for num in nums:
            ttl += num
            res += rem_to_cnt[ttl % k]
            rem_to_cnt[ttl % k] += 1
        
        return res
    


"""
prefix[i - 1] % k = prefix[j] % k
j  > i 
rem_to_cnt

"""