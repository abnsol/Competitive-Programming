class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        rem = 0
        while numBottles >= numExchange:
            ans += (numBottles // numExchange)
            numBottles = numBottles % numExchange + numBottles // numExchange
        
        return ans

        