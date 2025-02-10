# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def invert(self,arr):
        for i in range(len(arr)):
            arr[i] ^= 1
        return arr
            
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            flipped = list(reversed(image[i]))
            image[i] = self.invert(flipped)
        
        return image

        