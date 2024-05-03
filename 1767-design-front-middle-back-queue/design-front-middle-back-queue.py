class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
               
    def pushFront(self, val: int) -> None:
        self.queue.insert(0,val)        

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue)//2,val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue: 
            return self.queue.pop(0) 
        else:
            return -1       

    def popMiddle(self) -> int:
        if self.queue:
            if len(self.queue) % 2 == 0:
                popped = self.queue.pop(len(self.queue)//2 - 1)
            else:
                popped = self.queue.pop(len(self.queue)//2)
            return popped
        else: return -1 
        
    def popBack(self) -> int:
        if self.queue: 
            popped = self.queue.pop()
            return popped
        else: return -1 
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()