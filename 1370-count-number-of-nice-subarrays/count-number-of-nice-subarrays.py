class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = l = cnt = total = 0

        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                cnt += 1
                total = 0 
            
            while cnt == k:
                total += 1
                if nums[l] % 2 == 1:
                    cnt -= 1
                
                l += 1
            
            res += total
        
        return res
        