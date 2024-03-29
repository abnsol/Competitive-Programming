class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        j = count = res = 0
        maxElement = max(nums)
        for i in range(len(nums)):
            if nums[i] == maxElement:
                count += 1

            while count == k:               
                if nums[j] == maxElement:
                    count -= 1
                j += 1
            
            res += j
                
                
        return res

