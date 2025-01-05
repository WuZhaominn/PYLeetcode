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
    



递归步骤：
第一次调用： current = 1, prev = None

暂存 tmp = 2。
反转：1.next = None。
递归：self.reverse(2, 1)。
第二次调用： current = 2, prev = 1

暂存 tmp = 3。
反转：2.next = 1。
递归：self.reverse(3, 2)。
第三次调用： current = 3, prev = 2

暂存 tmp = 4。
反转：3.next = 2。
递归：self.reverse(4, 3)。
第四次调用： current = 4, prev = 3

暂存 tmp = 5。
反转：4.next = 3。
递归：self.reverse(5, 4)。
第五次调用： current = 5, prev = 4

暂存 tmp = None。
反转：5.next = 4。
递归：self.reverse(None, 5)。
第六次调用（递归结束）： current = None, prev = 5

返回 prev，即 5，作为反转后链表的新头节点。
