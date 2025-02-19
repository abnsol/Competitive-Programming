# Problem: Palindrome Linked List - https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow 
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        dummy = head
        while prev:
            if dummy.val != prev.val:
                return False
            dummy = dummy.next
            prev = prev.next
        
        return True

        