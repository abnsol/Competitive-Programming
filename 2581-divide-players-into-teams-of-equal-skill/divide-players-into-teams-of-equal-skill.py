class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)  
        l = 0 
        r = n - 1

        ans = 0
        chemo = skill[l] + skill[r]
        while l < r:
            ans += skill[l] * skill[r]
            if chemo != skill[l] + skill[r]:
                return -1
            l += 1
            r -= 1
        
        return ans