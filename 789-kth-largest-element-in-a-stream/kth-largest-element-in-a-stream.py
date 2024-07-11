class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.pq = []
        self.k = k 
        for num in nums:
            self.add(num)
               

    def add(self, val: int) -> int:
        if self.k > len(self.pq):
            heappush(self.pq,val)
        else:
            if self.pq[0] <= val:
                heappop(self.pq)
                heappush(self.pq,val)
        
        return self.pq[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)