class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        l = 0 
        while l < n:
            r =  n - 1
            m = l + 1
            while m < r:
                temp = nums[l] + nums[m] + nums[r]
                if temp > 0:
                    r -= 1
                elif temp < 0:
                    m += 1
                else:
                    ans.add(tuple([nums[l],nums[m],nums[r]]))
                    r -= 1
                    m += 1

            l += 1

        return ans
        