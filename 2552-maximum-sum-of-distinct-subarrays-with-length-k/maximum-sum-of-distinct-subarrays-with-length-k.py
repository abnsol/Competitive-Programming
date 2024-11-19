class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = ttl = 0
        n = len(nums)
        l = 0
        sett = set()
        for r in range(n):
            while nums[r] in sett or (r - l + 1) > k:
                sett.remove(nums[l])
                ttl -= nums[l]
                l += 1

            ttl += nums[r]
            sett.add(nums[r])
            if r - l + 1 == k:
                maxSum = max(ttl,maxSum)

        return maxSum

''' 
1 2 4 9 4 5 1
'''
        