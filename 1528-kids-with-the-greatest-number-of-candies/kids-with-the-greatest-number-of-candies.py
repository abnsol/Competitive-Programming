class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= max(candies))
        
        return result 