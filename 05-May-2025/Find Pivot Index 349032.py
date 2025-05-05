# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums) - 1
        ps = [0]
        ss = [0]

        for i in range(n):
            ps.append(nums[i] + ps[i])
            ss.append(nums[n - i] + ss[i])

        ss.reverse()
        for i in range(n + 1):
            if ps[i] == ss[i]:
                return i
        
        return -1

'''
[1,7,3,6,5,6]
[0, 1, 8, 11,17,22]
[27,20,17,11, 6,0]

[2,1,-1]
[0,2,3]
[0,]

intialize psa and ssa = 0
find ps starting with 0
find ss starting with 0

loop through the ps and ss to check for the pivot idx
return idx
'''