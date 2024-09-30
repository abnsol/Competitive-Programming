class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        numberCount = set()

        ops = 0
        for num in nums:
            numberCount.add(num)
            ops += len(numberCount) - 1
        
        return ops
        
        


'''
[5,1,3]
sort
1 find the min idx of largest element
2 prev largest idx
for i from min idx to last --> prev large (nsquare)
[1,1,3,5]
ops += 1
ops += 2
[1,1,1] --> 3

[1,1,2,2,3]
ops += 1
ops += 1
ops += 2
O(NlogN)
'''