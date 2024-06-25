class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(left,right):
            i,j = 0,0
            merged = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            merged += left[i:]
            merged += right[j:]
            return merged
        
        def mergesort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2
            left = mergesort(nums[:mid])
            right = mergesort(nums[mid:])
            return merge(left,right)
        
        return mergesort(nums)