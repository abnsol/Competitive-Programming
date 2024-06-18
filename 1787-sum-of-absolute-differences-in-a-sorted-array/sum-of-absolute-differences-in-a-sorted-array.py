class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n= len(nums)
        pre = [0]
        suf = [0] * n
        res = []
        
        for i in range(1,n):
            formula = i * (nums[i] - nums[i - 1]) + pre[i - 1]
            pre.append(formula)
        
        for j in range(n - 2,-1,-1):
            print(j)
            formula = (n - (j + 1)) * (nums[j + 1] - nums[j]) + suf[j + 1]
            suf[j] = formula
        
        for k in range(n):
            res.append(pre[k] + suf[k])
        
        return res

            