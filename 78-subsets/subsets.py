class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        
        def bt(idx):
            if idx >= len(nums):
                res.append(subset[:])
                return 
            
            # takeit 
            subset.append(nums[idx])
            bt(idx + 1)

            # leaveit
            subset.pop()
            bt(idx + 1)

        bt(0)
        return res
