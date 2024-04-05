class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAv = float('-inf')
        total = count = left = 0
        for right in range(len(nums)):
            total += nums[right]
            count += 1

            while count > k:
                total -= nums[left]
                left += 1
                count -= 1

            if count == k:
                maxAv = max(maxAv,total/k)
        return maxAv
                