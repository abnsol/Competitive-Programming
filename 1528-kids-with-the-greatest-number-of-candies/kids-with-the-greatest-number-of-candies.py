class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        for i in range(len(candies)):
            candies[i] = (candies[i] + extraCandies >= maxCandy)
        
        return candies