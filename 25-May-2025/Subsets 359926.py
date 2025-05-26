# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def bt(level,comb):
            if level == n:
                ans.append(comb[:])
                return
            comb.append(nums[level])
            bt(level + 1,comb)
            comb.pop()
            bt(level + 1,comb)
        
        bt(0,[])
        return ans