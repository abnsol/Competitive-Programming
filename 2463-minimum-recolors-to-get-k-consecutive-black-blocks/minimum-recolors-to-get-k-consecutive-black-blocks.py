class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minval = float('inf')
        count = countB = left = 0

        for i in range(len(blocks)):
            if blocks[i] == "W":
                countB += 1
            count += 1
            while count > k:
                if blocks[left] == "W":
                    countB -= 1
                count -= 1
                left += 1
            
            if count == k:
                minval = min(minval,countB)
        
        return minval


