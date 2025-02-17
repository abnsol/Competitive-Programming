# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # saves count of presums we got
        pre_count = Counter({0:1})
        ttl = ans = 0
        for num in nums:
            # add to presum
            ttl += num
            # is there a sum [we got before] from our dict that we can chop 
            ans += (pre_count[ttl - k])
            #add the sum to the dict
            pre_count[ttl] += 1
        return ans
    
    # can't be sliding cuz negative int
    # take brute force but its repetitive
    # what if i make the prefix sum prebuilt
    # so lets use simultaneous building and returning 

