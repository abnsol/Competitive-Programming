class Solution:
    def findMin(self, nums: List[int]) -> int:
        def findpivot(nums):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = (start + end)//2

                if mid < end and nums[mid] > nums[mid + 1]:
                    return mid
                if mid > start and nums[mid] < nums[mid - 1]:
                    return mid - 1
                if nums[start] > nums [mid]: 
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        pivot = findpivot(nums)
        return nums[pivot + 1]