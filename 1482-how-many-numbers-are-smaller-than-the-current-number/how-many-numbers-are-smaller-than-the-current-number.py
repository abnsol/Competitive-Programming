class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums) #nlogn
        ans = []        
        dictionary = {}

        for i in range(len(nums)): #n
            if sortedNums[i] not in dictionary:
                dictionary[sortedNums[i]] = i

        for num in nums:
            ans.append(dictionary[num])

        return ans 