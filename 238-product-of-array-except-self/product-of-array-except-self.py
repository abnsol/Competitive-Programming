class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * (n) 

        for i in range(1,n):
            ans[i] = nums[i - 1] * ans[i - 1]
        
        ss = 1 
        for j in range(n - 1,-1,-1):
            ans[j] *= ss
            ss *= nums[j]
        
        return ans

    
    # [1,1,2,6]  prefix product not including the current element
    # [24,12,4,1] suffix product not including the current 
    # [24,12,8,6]   multiply the prefix and suffix for the current element

    # [1,-1,-1,0,0]
    # [0,0,-9,3,0]
    # [0,0,9,0,0]


        