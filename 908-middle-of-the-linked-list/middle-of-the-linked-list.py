class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        length = 1
        while temp.next != None:
            temp = temp.next
            length += 1
        
        temp = head
        mid = length // 2
        for i in range(mid):
            temp = temp.next
        
        return temp