# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l ,r = 0, len(height) - 1
        ans = 0
        while l < r:
            area = min(height[l],height[r]) * (r - l)
            ans = max(ans,area)
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        
        return ans

        