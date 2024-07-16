class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxheap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if k > len(maxheap):
                    heappush(maxheap,-matrix[i][j])
                else:
                    heappushpop(maxheap,-matrix[i][j])
        
        return -maxheap[0]