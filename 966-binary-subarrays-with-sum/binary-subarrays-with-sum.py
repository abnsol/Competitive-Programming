class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashMap = {0 : 1}
        runningSum = 0
        res = 0

        for num in nums:
            runningSum += num
            if runningSum - goal in hashMap:
                res += hashMap[runningSum - goal]

            hashMap[runningSum] = hashMap.get(runningSum,0) + 1
        
        return res

        

'''
bf approach
O(n3)
optimized bf
O(n2)
[0,1,1,2,2,3]
j > i
ps[j] - ps[i] = goal
very optimized bf
O(N)
acc = 3
res = 4
{
    0 : 1,
    1 : 2,
    2 : 2,
    3 : 1
}

acc = 0
res = 15
{
    0 : 6,
}
'''