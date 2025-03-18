class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left=right=dummy = ListNode(next =head)
        for _ in range(n):
            right = right.next
        while right.next:
            left =left.next
            right = right.next
        left.next =left.next.next
        return dummy.next
