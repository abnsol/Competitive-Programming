class MyStack:

    def __init__(self):
        self.first = deque()
        self.second = deque()       

    def push(self, x: int) -> None:
        self.first.append(x)        

    def pop(self) -> int:
        for i in range(len(self.first) - 1):
            self.second.append(self.first.popleft())
        
        popped = self.first.popleft()

        while len(self.second) != 0:
            self.first.append(self.second.popleft())
        
        return popped       

    def top(self) -> int:
        for i in range(len(self.first) - 1):
            self.second.append(self.first.popleft())
        peeked = self.first.popleft()

        while len(self.second) != 0:
            self.first.append(self.second.popleft())
        self.first.append(peeked)
        return peeked 
        

    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()