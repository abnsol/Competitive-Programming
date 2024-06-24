class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def bt(ans,lis):
            if len(ans) == len(nums):
                res.append(ans[:])
                return
            
            for i in range(len(lis)):
                ans.append(lis[i])
                bt(ans,lis[:i] + lis[i + 1:])
                ans.pop()
            
        bt([],nums)
        return res

            

            

        