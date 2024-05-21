class Node:
    def __init__(self,val = 0,nxt = None):
        self.val = val
        self.next = nxt

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def get(self,idx):
        if idx < 0 or idx >= self.size: return -1
        dummy = self.head.next
        for _ in range(idx):
            dummy = dummy.next
        
        return dummy.val
    
    def addAtHead(self,val):
        return self.addAtIndex(0,val)
    
    def addAtTail(self,val):
        return self.addAtIndex(self.size,val)
    
    def addAtIndex(self,idx,val):
        if idx > self.size:
            return 
        
        pre = self.head
        for _ in range(idx):
            pre = pre.next
        
        node = Node(val,pre.next)
        pre.next = node
        self.size += 1
    
    def deleteAtIndex(self,idx):
        if idx < 0 or idx >= self.size:
            return
        
        pre = self.head
        for _ in range(idx):
            pre = pre.next
        
        delete = pre.next
        pre.next = delete.next
        delete.next = None
        self.size -= 1        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)