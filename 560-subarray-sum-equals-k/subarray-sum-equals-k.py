class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc = 0
        count = {0 : 1} # store the previous results that can be subrtracted
        res = 0

        for num in nums:
            acc += num
            if acc - k in count:
                res += count[acc - k]
            
            count[acc] = count.get(acc,0) + 1

        return res 

'''
brute force approach
find every sub array
find the sum of those sub arrays
check equal with k

optimized bf
ps = [0,1,2,3]

O(n) => prefixsum approach with hashmap
ps = [0,1,2,3]
res = 0
0 : 1
1 : 1
2 : 1 res = 1
3 : 1 res = 2
'''