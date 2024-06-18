class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        while tickets[k] != 0:
            for j in range(len(tickets)):
                if tickets[j] > 0:
                    ans += 1
                    tickets[j] -= 1
                if tickets[k] == 0:
                    break
        
        return ans
