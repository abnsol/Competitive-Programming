# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for key in count:
            ans +=  ceil(count[key]/(key + 1)) * (key + 1) 
                
            
        return ans