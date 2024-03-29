class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left , right = 0, len(skill) - 1
        equals =  skill[left] + skill[right]
        products = []
        while left < right:
            temp = skill[left] + skill[right]
            if temp != equals:
                return -1
            else:
                products.append(skill[left] * skill[right])
                left += 1
                right -= 1
        return sum(products)
        