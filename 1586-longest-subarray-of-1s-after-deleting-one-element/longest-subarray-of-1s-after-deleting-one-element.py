class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        oneCounter = zeroCounter = maxLength = l = 0
        n = len(nums)
        setLength = len(set(nums))

        if setLength == 1 and nums[0] == 1:
            return n - 1
        
        if  setLength == 1 and nums[0] == 0:
            return maxLength

        for r in range(n):
            if nums[r] == 1:
                oneCounter += 1
            else:
                zeroCounter += 1
            
            while zeroCounter > 1:
                if nums[l] == 0:
                    zeroCounter -= 1
                else:
                    oneCounter -= 1
                
                l += 1
            
            maxLength = max(maxLength,oneCounter)
        
        return maxLength


'''
dynamic sliding window approach
initialize oneCounter,zeroCounter,maxLength
intialize l = 0
for r in len(nums):
    if nums[r] == 1:
        oneCounter += 1
    else:
        zeroCounter += 1
    
    while zeroCounter > 1:
        if nums[l] == 0:
            zeroCounter -= 1
        else:
            oneCounter -= 1
    
    maxlength = max(oneCounter,maxlength)

return maxLength
'''