class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = Counter({0 : 1})
        acc = 0
        res = 0

        for num in nums:
            acc += num
            res += cnt[acc - k]
            cnt[acc] += 1

        return res            

'''
0 > 1
1 > 1
2 > 1


acc = 1
res = 0

acc = 2
res = 1

acc = 3
res = 2
'''