class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        if numOnes > k: return k
        while k > 0:
            if numOnes > 0:
                ans += numOnes
                k -= numOnes
                numOnes = 0
            elif numZeros > 0:
                k -= 1
                numZeros -= 1
            else:
                ans += -1
                k -= 1
                numNegOnes -= 1
            
        return ans