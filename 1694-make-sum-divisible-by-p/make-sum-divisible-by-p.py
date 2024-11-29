class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        ttl = sum(nums)
        # prefix[i] % p == prefix[j] % p
        remainder = ttl % p

        if remainder == 0:
            return 0 

        res = len(nums)
        cur_sum = 0
        # save rem mod to where they appear last 
        # looking for this to remove from arr to make sum div by p
        remainderMod = {0 : -1} 

        for idx,num in enumerate(nums):
            cur_sum = (cur_sum + num) % p
            # target = cur_sum - remainder
            # this is the maths to find the number we want to remove from the 
            # current sum remainder to make the remaining sum div by p
            prefix = (cur_sum - remainder + p) % p
            if prefix in remainderMod:
                length = idx - remainderMod[prefix] # length of subarray
                res = min(length,res)
            
            remainderMod[cur_sum] = idx

        return -1 if res == len(nums) else res 

