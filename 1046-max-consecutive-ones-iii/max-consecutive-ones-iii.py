class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxRes = count = l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1
                l += 1

            maxRes = max(maxRes, r - l + 1)

        return maxRes


        