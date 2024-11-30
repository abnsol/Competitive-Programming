class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.q = deque()
        self.countInsert = 0
        self.countElements = {}

    def consec(self, num: int) -> bool:
        self.q.append(num)
        self.countInsert += 1
        self.countElements[num] = self.countElements.get(num,0) + 1
        if self.countInsert > self.k:
            popped = self.q.popleft()
            self.countElements[popped] -= 1
            self.countInsert -= 1
        
        return self.countElements[self.q[0]] == self.k and self.q[0] == self.value

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
'''
'''