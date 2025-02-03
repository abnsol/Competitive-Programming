# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        elem = {}
        for w,l in matches:
            if w not in elem:
                elem[w] = 0
            if l not in elem:
                elem[l] = 0
            
            elem[l] += 1
        
        winner = []
        loser = []
        for player in elem:
            if elem[player] == 0:
                winner.append(player)
            elif elem[player] == 1:
                loser.append(player)
        
        return [sorted(winner),sorted(loser)]
