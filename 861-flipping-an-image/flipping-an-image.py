class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        idx = 0
        for row in image:
            row.reverse()
            while idx < len(row):
                row[idx] ^= 1
                idx += 1
            idx = 0

        return image


