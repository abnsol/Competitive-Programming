class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = len(nums)

        def minimum():
            minVal = 0
            for i in range(n):
                if nums[i] < nums[minVal]:
                    minVal = i
            
            return minVal
        
        for i in range(k):
            minVal = minimum()
            print(minVal)
            nums[minVal] = nums[minVal] * multiplier
        
        return nums



"""
FOR loop
    min() => return Idx
"""
        