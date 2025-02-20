# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode("Dum",head)
        fast = dummy_head
        for i in range(n + 1):
            fast = fast.next
        
        slow = dummy_head
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy_head.next