class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingtime = 0
        delay = 0

        for a,t in customers:
            if delay - a <= 0:
                delay = a + t
                waitingtime += delay - a
            else:
                waitingtime += delay - a + t
                delay += t
        
        return waitingtime/len(customers)
            
            
        
       