class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,len(nums) - 1
        ans = 0
        print(nums)
        while l < r:
            ttl = nums[l] + nums[r]
            if ttl > k:
                r -= 1
            elif ttl < k:
                l += 1
            else:
                ans += 1
                l += 1
                r -= 1

        return ans 
        