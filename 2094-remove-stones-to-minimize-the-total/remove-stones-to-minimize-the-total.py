class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = []
        for pile in piles:
            heappush(maxheap,-pile)
        
        while k > 0:
            pile = heappop(maxheap)
            heappush(maxheap,floor(pile/2))
            k -= 1
        
        return -sum(maxheap)