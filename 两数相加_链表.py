# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #哨兵结点，简化链表操作，指向结果链表的表头
        dummy=ListNode(0)
        node = dummy
        carry =0
        while carry or l1 or l2:
            #如果 l1 不为空，将 l1 当前节点的值加到 carry 中，并移动到 l1 的下一个节点。
            if l1:
                carry+=l1.val
                l1=l1.next
            if l2:
                carry+=l2.val
                l2=l2.next
            node.next = ListNode(carry%10)
            carry //=10
            node =node.next
        return dummy.next
