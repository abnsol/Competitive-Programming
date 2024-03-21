class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        maxItem = max(nums)
        count = [0] * (maxItem + 1)

        for num in nums:
            count[num] += 1

        print(count)
        prefix = 0
        for _ in range(len(count)):
            temp = count[_]
            count[_] = prefix
            prefix += temp 
        
        print(count)
        ans = []
        for num in nums:
            ans.append(count[num])

        return ans
