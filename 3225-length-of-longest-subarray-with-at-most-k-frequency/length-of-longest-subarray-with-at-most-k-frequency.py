class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        j = 0
        count = {}
        res = 0
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
            while count[nums[i]] > k:
                count[nums[j]] -= 1
                j += 1
            
            res = max(res,i - j + 1)
        return res
