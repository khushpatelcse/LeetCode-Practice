//Approach - Iterate through each of the linked lists provided until they are both null, and the tens place carry is null. In each iteration, add the sum of the two corresponding nodes and the carry to a node in the new linked list, and replace the old carry with a newly calculated carry. Return the real head, tempHead.next.
public class ListNode {

    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

public class AddTwoNumbers_P2 {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode tempHead = new ListNode();
        ListNode tail = tempHead;
        int carry = 0;

        while (l1 != null || l2 != null || carry != 0) {
            int num1 = 0;
            int num2 = 0;
            if (l1 != null) {
                num1 = l1.val;
            }
            if (l2 != null) {
                num2 = l2.val;
            }

            int sum = num1 + num2 + carry;

            tail.next = new ListNode(sum % 10);
            tail = tail.next;

            carry = sum / 10;

            if (l1 != null) {
                l1 = l1.next;
            }
            if (l2 != null) {
                l2 = l2.next;
            }
        }
        return tempHead.next;
    }
}
