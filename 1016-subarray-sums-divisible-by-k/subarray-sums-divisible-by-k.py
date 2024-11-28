class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cnt = Counter({0 : 1})
        ttl = 0
        res = 0

        for i in nums:
            ttl += i
            res += cnt[ttl % k]
            cnt[ttl % k] += 1
        
        return res

'''
brute force
find every subarray
find the sum of each subarray and check if div by k
increment result
O(n3)

[0,4,9,9,7,4,5] O(n2)
(prefix[j] - prefix[i]) % k == 0

prefix sum approach
prefix[j] % k == prefix[i] % k
'''
        