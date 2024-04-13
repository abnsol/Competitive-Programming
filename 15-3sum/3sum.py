class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        l = 0 
        right = len(nums) - 1
        while l < len(nums):
            r = right 
            m = l + 1
            while m < r:
                if nums[l] + nums[m] + nums[r] > 0:
                    r -= 1
                elif nums[l] + nums[m] + nums[r] < 0:
                    m += 1
                else:
                    temp = [nums[l],nums[m],nums[r]]
                    ans.add(tuple(temp))
                    r -= 1
                    m += 1
            l += 1

        return ans
        