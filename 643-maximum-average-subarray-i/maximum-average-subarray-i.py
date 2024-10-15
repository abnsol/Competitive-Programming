class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        windowSum = sum(nums[:k])
        maxSum = windowSum

        for i in range(k,n):
            windowSum += nums[i] - nums[i - k]
            maxSum = max(windowSum,maxSum)
        
        return maxSum/k


'''
fixed sliding window 
maximum sum of k fixed window
intalize maxSum = -infinity
intialze l & r = 0 & k
while r < n:
    maxSum = max(maxSum,sum(arr[l:r]))
    l++
    r++
return maxSum/k
'''