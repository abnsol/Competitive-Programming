class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        acc = 0
        sufAcc = 0
        n = len(nums)

        for i in range(n):
            pre.append(acc)
            suf.append(sufAcc)
            acc += nums[i]
            sufAcc += nums[n - i - 1]
       
        suf.sort(reverse=True)
        ans = []
        for i in range(n):
            res = 0
            res += nums[i] * i - pre[i]
            res += abs(suf[i] - nums[i] * (n - i - 1))
            ans.append(res)
    
        return ans



'''
[2,1,2]
[0,2,5]
[8,5,0]
'''