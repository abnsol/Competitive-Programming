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


