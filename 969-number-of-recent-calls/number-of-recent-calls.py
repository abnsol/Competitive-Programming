class RecentCounter:

    def __init__(self):
        self.q = []
        self.length = 0

    def ping(self, t: int) -> int:
        while self.q and t - self.q[0] > 3000:
            self.q.pop(0)
            self.length -= 1

        self.q.append(t)
        self.length += 1
        return self.length 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)