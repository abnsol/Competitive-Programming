class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0

        for i in range(len(costs)):
            if coins - costs[i] < 0:
                return ans
            elif coins - costs[i] == 0:
                return ans + 1
            else:
                coins -= costs[i]
                ans += 1
        
        return ans

