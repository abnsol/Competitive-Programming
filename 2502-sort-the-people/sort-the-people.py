class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)
        height_to_names = {}
        for i in range(n):
            height_to_names[heights[i]] = names[i]
        
        heights.sort()
        for i in range(n):
            names[i] = height_to_names[heights[n - i - 1]]
        
        return names
        