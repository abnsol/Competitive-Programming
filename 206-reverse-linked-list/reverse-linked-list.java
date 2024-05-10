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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode pres = head;
        ListNode nxt;
        if (head != null) {
            nxt = head.next;
            }
        else return head;

        while (nxt != null){
            pres.next = prev;
            prev = pres;
            pres = nxt;
            nxt = nxt.next;
        }
        pres.next = prev;
        return pres; 
    }
}