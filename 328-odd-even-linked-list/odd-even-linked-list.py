# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headodd = head
        dummyodd = head
        if head is not None:
            dummyeven = head.next
            headeven = dummyeven
        else:
            return head
        
        while dummyeven is not None and dummyeven.next is not None:
            node =  dummyodd.next.next
            nodetwo = dummyeven.next.next
            dummyodd.next = dummyodd.next.next
            dummyeven.next = dummyeven.next.next
            dummyodd = node
            dummyeven = nodetwo
        
        if dummyodd.next is not None and dummyodd.next.next is not None: 
            dummyodd.next = dummyodd.next.next
            dummyodd = dummyodd.next.next
        
        dummyodd.next = headeven
        return headodd


