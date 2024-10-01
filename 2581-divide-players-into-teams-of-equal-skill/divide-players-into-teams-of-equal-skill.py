class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        requiredSkill = skill[0] + skill[-1]
        totalChemistry = skill[0] * skill[-1]
        l, r = 1, len(skill) - 2

        while l < r:
            if skill[l] + skill[r] != requiredSkill:
                return -1

            totalChemistry += skill[l] * skill[r]
            l += 1
            r -= 1

        return totalChemistry


'''
Two pointers approach
 sort
 intialize my pointers
 iterate through the array
 previous skill = 6
 totalchemistry = 0
 check if sum of skills is equal with previous skill sum
        not : return  -1
        is: continue
            increment tc by product of team skill
 
 return total chemistry here

1 2 3 3 4 5 

'''