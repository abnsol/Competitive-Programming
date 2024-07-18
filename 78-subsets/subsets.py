class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def bt(idx,arr):
            if idx > len(nums):
                return 
            
            if arr not in ans:
                ans.append(arr[:])
            
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                bt(i + 1,arr)
                arr.pop()
        
        
        for i in range(len(nums)):
            bt(i,[])
        return ans
