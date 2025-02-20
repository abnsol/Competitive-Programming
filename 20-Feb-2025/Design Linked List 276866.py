# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if self.size <= index:
            return -1

        dummy = self.head
        for i in range(index):
            dummy = dummy.next
        return dummy.val

    def addAtHead(self, val: int) -> None:
        return self.addAtIndex(0,val)

    def addAtTail(self, val: int) -> None:
        return self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        dummy_head = Node("Dum",self.head)
        curr = dummy_head
        node = Node(val)

        if index > self.size:
            return

        for i in range(index):
            curr = curr.next
        
        if curr:
            node.next = curr.next
            curr.next = node

        self.size += 1
        self.head = dummy_head.next if index == 0 else self.head
    
    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return 
        
        dummy_head = Node("Dum",self.head)
        curr = dummy_head
        
        for i in range(index):
            curr = curr.next
        
        if curr.next:
            curr.next = curr.next.next
        
        self.head = self.head.next if index == 0 else self.head
        self.size = self.size - 1 if self.size >= 1 else 0

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)