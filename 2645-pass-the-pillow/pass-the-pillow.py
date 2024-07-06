class Solution:
    def passThePillow(self, n, time):
       
        full_rounds = time // (n - 1)
        extra_time = time % (n - 1)
        if full_rounds % 2 == 0:
            return extra_time + 1  
        else:
            return n - extra_time  