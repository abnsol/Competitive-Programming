class Solution:
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)

    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            subgcd = nums[i]
            if subgcd == k:
                count += 1

            for j in range(i + 1,len(nums)):
                subgcd = gcd(subgcd,nums[j])
                if subgcd == k:
                    count += 1           
                                    
        return count

            
        