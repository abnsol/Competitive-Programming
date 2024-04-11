class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        newImage = []
        n = len(image)
        for i in range(n):
            temp = image[i][::-1]
            for j in range(n):
                temp[j] = ~temp[j] & 1
            newImage.append(temp)
        return newImage


