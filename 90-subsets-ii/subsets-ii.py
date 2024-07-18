class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def bt(idx,arr):
            if idx == n:
                if sorted(arr) not in ans:
                    ans.append(sorted(arr)[:])
                    return
            
            if sorted(arr) not in ans:
                ans.append(sorted(arr)[:])
            
            for i in range(idx,n):
                arr.append(nums[i])
                bt(i + 1,arr)
                arr.pop()
            
        bt(0,[])
        return ans
                
