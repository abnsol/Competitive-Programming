class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []        

    def push(self, x: int) -> None:
        self.first.append(x)       

    def pop(self) -> int:
        while len(self.first) != 0:
            self.second.append(self.first.pop())
        
        popped = self.second.pop()
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        
        return popped      

    def peek(self) -> int:
        while len(self.first) != 0:
            self.second.append(self.first.pop())
        peeked = self.second[-1]
        while len(self.second) != 0:
            self.first.append(self.second.pop())
        
        return peeked
        
    def empty(self) -> bool:
        return len(self.first) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()