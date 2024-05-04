class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        ans = 0
    
        while l <= r:
            if l == r: 
                ans += 1
                l += 1
            elif people[l] + people[r] == limit:
                ans += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                ans += 1
                r -= 1
            elif people[l] + people[r] < limit:
                while l < r:
                    if people[l] + people[r] <= limit:
                        ans += 1
                        l += 1
                        r -= 1
                    else:
                        ans += 1
                        r -= 1
        return ans
