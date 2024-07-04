# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = None
        while head.next:
            val = 0
            head = head.next
            while head.val != 0:
                val += head.val
                head = head.next
            
        
            if not ans:
                ans = ListNode(val)
                temp = ans
            else:
                temp.next = ListNode(val)
                temp = temp.next
        
        return ans
            

            

        
