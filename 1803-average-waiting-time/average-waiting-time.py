class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        waitingtime = 0
        ttl = 0
        

        for a,t in customers:
            if ttl - a <= 0:
                ttl = a + t
                waitingtime += t
            else:
                ttl += t
                waitingtime += ttl - a
                
        
        return waitingtime/n
            
            
        
       