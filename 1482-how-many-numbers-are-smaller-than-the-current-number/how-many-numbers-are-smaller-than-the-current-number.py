class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # count sort implementation

        count = [0] * (max(nums) + 1)

        for num in nums:
            count[num] += 1

        prefix = 0
        for _ in range(len(count)):
            temp = count[_]
            count[_] = prefix
            prefix += temp 

        ans = []
        for num in nums:
            ans.append(count[num])

        return ans
