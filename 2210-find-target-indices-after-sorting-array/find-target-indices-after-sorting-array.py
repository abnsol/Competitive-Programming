class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        start, end= 0, len(nums) - 1

        while start <= end:
            mid = start + (end - start)//2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                while mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                    mid += 1
                end = mid
                while mid > 0 and nums[mid] == nums[mid - 1]:
                    mid -= 1
                start = mid
                return list(range(start,end + 1))
            

        