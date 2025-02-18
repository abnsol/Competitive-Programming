# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prev_sum = Counter({0 : 1})
        ttl = ans = 0
        for num in nums:
            ttl += num
            ans += prev_sum[ttl - goal]
            prev_sum[ttl] += 1
        return ans
        