# Problem: Partition List - https://leetcode.com/problems/partition-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy_before = ListNode(0,None)
        before = dummy_before
        dummy_after = ListNode(0,None)
        after = dummy_after

        while head:
            if head.val >= x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next

            head = head.next

        after.next = None
        before.next = dummy_after.next
        return dummy_before.next  