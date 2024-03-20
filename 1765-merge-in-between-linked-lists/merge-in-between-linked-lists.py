class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1