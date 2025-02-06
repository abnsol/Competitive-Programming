# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        intial = sum(i for i in nums if i % 2 == 0)
        
        for v,i in queries:
            ttl = nums[i] + v
            if ttl % 2 == 0:
                if nums[i] % 2 != 0:
                    intial += ttl
                else:
                    intial += v
            else:
                if nums[i] % 2 == 0:
                    intial -= nums[i]
            
            nums[i] = ttl 
            ans.append(intial)
        
        return ans
        
        