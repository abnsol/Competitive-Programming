class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ps = [1]
        ss = [1]
        n = len(nums)
        psp = ssp = 1
        for i in range(n - 1):
            psp *= nums[i]
            ssp *= nums[n - i - 1]
            ps.append(psp)
            ss.append(ssp)
        
        ss.reverse()
        ans = []
        for i in range(n):
            ans.append(ps[i] * ss[i])
        
        return ans


'''
[1,2,3,4]

[4,3,2,1]
[1,4,12,24]
[1,1,2,6]
[24,12,4,1]
[24,12,8,6]

algorithm

init ps and ss and ans
loop through and calculate ps and ss
mul ss[i] ps[i] > ans

[-1,1,0,-3,3]
[1,-1,-1,0,0]
[0,0,-9,3,1]
[0,0,9,0,0]
'''