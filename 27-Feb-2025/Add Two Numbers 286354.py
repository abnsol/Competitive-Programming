# Problem: Add Two Numbers - https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        dummy_ans, dummy_l1, dummy_l2 = ans, l1, l2
        rem = 0

        while dummy_l1 or dummy_l2:
            res = rem
            if dummy_l1 and dummy_l2:
                res += (dummy_l1.val + dummy_l2.val)
                dummy_l1 = dummy_l1.next
                dummy_l2 = dummy_l2.next      
            elif dummy_l1:
                res += dummy_l1.val
                dummy_l1 = dummy_l1.next
            elif dummy_l2:
                res += dummy_l2.val
                dummy_l2 = dummy_l2.next      
            
            rem = 1 if res > 9 else 0
            dummy_ans.next = ListNode(res % 10)
            dummy_ans = dummy_ans.next
        
        dummy_ans.next = ListNode(1) if rem else None
        
        return ans.next

