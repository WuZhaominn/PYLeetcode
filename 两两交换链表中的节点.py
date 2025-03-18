class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node0 = dummy = ListNode(next =head)
        node1 = head
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next


            node0.next = node2    #0->2
            node2.next = node1    #2->1
            node1.next = node3    #1->3


            node0 =node1
            node1 =node3
        return dummy.next
