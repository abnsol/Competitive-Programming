# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        dummy = head
        while dummy is not None:
            stack.append(dummy.val)
            dummy = dummy.next
        
        second = head
        while second is not None:
            if second.val != stack.pop():
                return False
            second = second.next
        return True