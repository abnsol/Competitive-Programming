class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ttl = 0
        remMod = { 0 : -1 }

        for idx,num in enumerate(nums):
            ttl += num
            remainder = ttl % k
            if remainder not in remMod:
                remMod[remainder] = idx
            elif idx - remMod[remainder] > 1:
                return True
                
        
        return False
        
'''
23 2 4 6 7
bruteforce
O(n2)
optimize bf
[]
(prefix[j] - prefix[i]) % k == 0
j > i
sum elements b/n j and i is divisible by 6
[0,23,25,29,35,42] 
optimize ps
prefix[j] % k == prefix[i] % k
hashmap => remMod : idx
idx - hashMap[prefix[j] % k] > 1
{
    0 : -1
    5 :  0
    1 :  1
}
'''