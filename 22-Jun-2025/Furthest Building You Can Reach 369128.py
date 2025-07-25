# Problem: Furthest Building You Can Reach - https://leetcode.com/problems/furthest-building-you-can-reach/

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                continue
                
            heappush(pq, diff)
            if len(pq) > ladders:
                bricks -= heappop(pq)
            if bricks < 0:
                return i

        return len(heights) - 130