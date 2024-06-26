class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        count = [0]
        def merge(left,right):
            l,r = 0,0
            while l < len(left) and r < len(right):
                if left[l] > 2 * right[r]:
                    count[0] += len(left) - l
                    r += 1
                else:
                    l += 1

            l,r = 0,0
            merged = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    merged.append(left[l])
                    l += 1
                else:
                    merged.append(right[r])
                    r += 1
            
            merged += left[l:]
            merged += right[r:]
            return merged      

        
        def mergesort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr)//2
            left = mergesort(arr[:mid])
            right = mergesort(arr[mid:])

            return merge(left,right)
        
        mergesort(nums)
        return count[0]

'''

'''