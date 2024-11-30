class RecentCounter:

    def __init__(self):
        self.q = []
        

    def ping(self, t: int) -> int:
        while self.q and t - self.q[0] > 3000:
            self.q.pop(0)

        self.q.append(t)
        return len(self.q) 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)