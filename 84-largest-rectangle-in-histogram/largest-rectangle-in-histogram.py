class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for index , height in enumerate(heights):
            start = index
            while stack and stack[-1][1] > height:
                idx , h = stack.pop()
                maxArea = max(maxArea,(index - idx) * h)
                start = idx 
            
            stack.append((start,height))
        
        for index , height in stack:
            maxArea = max(maxArea,(len(heights) - index) * height)
        
        return maxArea
                        