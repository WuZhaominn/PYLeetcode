#迭代
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev

#递归
class Solution:
    def reverse(self,current:ListNode,prev:ListNode) ->ListNode:
        if not current:
            return prev
        tmp = current.next
        current.next = prev
        return self.reverse(tmp,current)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head, None)
    
