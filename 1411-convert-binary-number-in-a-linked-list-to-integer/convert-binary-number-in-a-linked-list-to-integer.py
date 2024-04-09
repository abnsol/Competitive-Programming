# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
            
        idx = res = 0
        for i in range(len(arr) - 1, -1, -1):
            res += (arr[i] * (2 ** idx))
            idx += 1
        
        return res
        