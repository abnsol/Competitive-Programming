class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        unique = set()
        maxScore = currscore = left = 0
        for i in range(len(nums)):
            currscore += nums[i]
            while nums[i] in unique:
                currscore -= nums[left]
                unique.remove(nums[left])
                left += 1

            unique.add(nums[i])
            maxScore = max(maxScore,currscore)

        return maxScore


                

