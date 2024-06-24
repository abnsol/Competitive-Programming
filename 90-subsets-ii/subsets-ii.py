class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(idx,ans):
            if len(nums) == idx:
                res.append(ans[:])
                return

            ans.append(nums[idx])
            bt(idx + 1,ans)
            ans.pop()
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            bt(idx + 1,ans)

        bt(0,[])
        return res