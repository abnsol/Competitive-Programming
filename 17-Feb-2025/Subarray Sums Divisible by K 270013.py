# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # if rem the same then the pre is divisible by k
        rem_idx = Counter({0:1})
        ttl = ans = 0
        for num in nums:
            ttl += num
            ans += rem_idx[ttl % k]
            rem_idx[ttl % k] += 1
        return ans