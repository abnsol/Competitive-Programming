class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float("-inf")
        ps = 0
        for num in nums:
            ps += num
            if ps < 0:
                res = max(res,ps)
                ps = 0
            else:
                res = max(res,ps)

        return res



'''
ps < 0 reset to zero
max = (res,acc)
'''