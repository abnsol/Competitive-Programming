# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_prod = 1        
        suf_prod = 1
        pre = []
        suf = []

        for i in range(n):
            pre.append(pre_prod)
            pre_prod *= nums[i]
            suf.append(suf_prod)
            suf_prod *= nums[n - 1 - i]
        suf.reverse()
        
        # print(pre,suf)
        return [suf[i] * pre[i] for i in range(len(nums))]


        