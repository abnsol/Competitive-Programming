class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums,target,boolean):
            ans = -1
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    ans = mid
                    if boolean:
                        high = mid - 1
                    else:
                        low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return ans
        
        ans = [-1,-1]
        first = search(nums,target,True)
        last = search(nums,target,False)
        ans[0] = first
        ans[1] = last

        return ans
            
