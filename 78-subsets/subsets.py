class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def bt(idx,arr):
            if idx == len(nums):
                ans.append(arr[:])
                return 
            
            ans.append(arr[:])
            
            for i in range(idx,len(nums)):
                arr.append(nums[i])
                bt(i + 1,arr)
                arr.pop()
        
        bt(0,[])
        return ans
