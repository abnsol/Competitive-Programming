# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_idx = Counter({0:-1})
        ttl = 0
        for idx,num in enumerate(nums):
            ttl += num
            if ttl % k in rem_idx and idx - rem_idx[ttl % k] > 1:
                return True
            if ttl % k not in rem_idx:
                rem_idx[ttl % k] = idx
        
        return False
        