# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        pres = head
        if head is not None:nxt = head.next
        else: return head

        while nxt is not None:
            pres.next = prev
            prev = pres
            pres = nxt
            nxt = nxt.next

        pres.next = prev
        return pres
