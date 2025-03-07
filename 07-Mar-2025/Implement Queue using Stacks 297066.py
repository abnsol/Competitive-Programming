# Problem: Implement Queue using Stacks - https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.first = []
        self.second = []        

    def push(self, x: int) -> None:
        self.first.append(x)        

    def pop(self) -> int:
        while self.first:
            self.second.append(self.first.pop())
        
        popped = self.second.pop()
        while self.second:
            self.first.append(self.second.pop())

        return popped        

    def peek(self) -> int:
        while self.first:
            self.second.append(self.first.pop())
        
        peeked = self.second[-1]
        while self.second:
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