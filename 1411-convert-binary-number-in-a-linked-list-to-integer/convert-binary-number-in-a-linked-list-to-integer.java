/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int getDecimalValue(ListNode head) {
        List<Integer> arr = new ArrayList<>();
        while (head != null){
            arr.add(head.val);
            head = head.next;
            }
        
        int idx = 0, res = 0; 
        for (int i = arr.size() - 1; i >= 0; i--){
            res += (arr.get(i) * Math.pow(2,idx));
            idx++;
        }

        return res;
    }
}