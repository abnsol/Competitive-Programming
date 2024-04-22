class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # pigeonhole principle
        cnt = Counter({0 : 1})   # keep track of the remainders , empty subarray is divisible by k
        ans = ttl = 0            # answer and running sum 

        for num in nums:
            ttl += num             
            ans += cnt[ttl % k]   # wiz that running sum it can make cnt[ttl % k] subarrays of sum divisible by k 
            cnt[ttl % k] += 1
        
        return ans
        
# i            j
# [0,4,9,0,7,4,5]
# (ps[j] - ps[i]) % k == 0  --> ps[i] == ps[j] --- (*)
# what if % k != 0
# ps[j] % k = R1 --> ps[j] = A * k + R1      
# ps[i] % k = R2 --> ps[i] = B * K + R2
# ps[j] - ps[i] = A * k + R1 - (B * k + R2)
#               = (A - B) * k + (R1 - R2)  
#               = (A - B) * k               assume R1 = R2
# so a property to notice here if R1 == R2 then prefix sums can be divisible by k