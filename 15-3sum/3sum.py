class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()
        l = 0
        m = 1
        r = n - 1

        while l < r:
            target = nums[l]
            while m < r:
                if target + nums[m] + nums[r] == 0:
                    ans.add(tuple([target,nums[m],nums[r]]))
                    m += 1
                    r -= 1
                elif  target + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    m += 1
            
            l += 1
            m = l + 1
            r = n - 1
        
        return list(ans)
        