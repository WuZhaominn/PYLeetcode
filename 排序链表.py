class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        #找到链表的中间节点
        slow,fast = head,head.next
        while fast and fast.next:
            fast,slow = fast.next.next,slow.next
        mid,slow.next = slow.next,None
        #递归排序
        left,right = self.sortList(head),self.sortList(mid)
        h = res = ListNode(0)
        while left and right:
            if left.val< right.val:
                h.next,left = left,left.next
            else:
                h.next,right = right,right.next
            h = h.next
        if left:
            h.next =left 
        else:
            h.next =right
        return res.next
