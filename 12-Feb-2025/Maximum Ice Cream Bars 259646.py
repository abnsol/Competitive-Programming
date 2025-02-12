# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxx = max(costs) + 1
        cnt = [0] * maxx

        for num in costs:
            cnt[num] += 1
        
        i = ans = 0
        print(cnt)
        while i < maxx and coins > 0:
            while cnt[i] > 0 and coins >= i and coins > 0:
                ans += 1
                coins -= i
                cnt[i] -= 1
            i += 1
        
        return ans
                
        