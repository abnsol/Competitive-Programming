# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        l ,r = 0, n - 1
        print(people)

        ans = 0
        while l < r:
            ttl = people[l] + people[r]
            if ttl > limit:
                r -= 1
            elif ttl <= limit:
                l += 1
                r -= 1
                            
            ans += 1
        
        if l == r:
            ans += 1
            
        return ans
