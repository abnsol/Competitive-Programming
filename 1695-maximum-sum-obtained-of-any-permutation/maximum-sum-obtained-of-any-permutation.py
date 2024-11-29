class Solution:
    def maxSumRangeQuery(self, nums: List[int], req: List[List[int]]) -> int:
        n = len(nums)
        mod = 10 ** 9 + 7
        rangeUpdate = [0] * (n + 1)
        for start,end in req:
            rangeUpdate[start] += 1
            rangeUpdate[end + 1] -= 1
        
        acc = 0
        for i in range(n):
            acc += rangeUpdate[i]
            rangeUpdate[i] = acc
        
        nums.sort()
        last_element = rangeUpdate[-1]
        rangeUpdate = sorted(rangeUpdate[:-1]) + [last_element]

        ans = 0
        for i in range(n):
            ans = (ans + nums[i] * rangeUpdate[i]) % mod
        
        return ans


'''
bruteforce => O(n3)
prefix Sum approach
[1,3,6,10,15]
sum(1,3) = ps[end] - ps[start]
'''