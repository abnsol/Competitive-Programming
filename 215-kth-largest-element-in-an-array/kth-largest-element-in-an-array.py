class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []

        for i in nums:
            if len(minheap) < k:
                heapq.heappush(minheap,i)
            else:
                heapq.heappush(minheap,i)
                heapq.heappop(minheap)
        
        return minheap[0]
                
