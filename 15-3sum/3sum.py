class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        l, m ,r = 0, 1, n - 1
        ans = set()

        while l < r:
            target = nums[l]
            while m < r:
                if target + nums[m] + nums[r] == 0:
                    triplet = [nums[l],nums[m],nums[r]]
                    ans.add(tuple(triplet))
                    m += 1
                    r -= 1
                elif target + nums[m] + nums[r] > 0:
                    r -= 1
                else:
                    m += 1
            
            l += 1
            m = l + 1
            r = n - 1
        
        return ans
