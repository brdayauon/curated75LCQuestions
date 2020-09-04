// /**
//  * Definition for singly-linked list.
//  * public class ListNode {
//  *     int val;
//  *     ListNode next;
//  *     ListNode(int x) { val = x; }
//  * }
//  */

public class ListNode{
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
class Solution {
    public ListNode reverseList(ListNode head) {
        //initialize pointers
        ListNode prev = null;
        ListNode curr = head;
        
        //traverse head
        while(curr != null){
            //save state
            ListNode nxt = curr.next;
            //reversing
            curr.next = prev;
            //update the pointers
            prev = curr;
            curr = nxt;
        }
        //return the new head 
        return prev;
    }
}