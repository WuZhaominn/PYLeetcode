class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #r 和 fast 都指向链表的头节点 head。
        #l 用来存储反转后的链表的头节点，初始为 None。
        slow = fast = head
        l = None
        while fast and fast.next:
            fast = fast.next.next
            a = slow.next
            slow.next = l
            l = slow
            slow = a
        #判断链表是否是奇数长度。如果 fast 在终止时指向的是一个有效节点（即链表长度是奇数），那么 r 需要向后移动一位，跳过中间的元素。
        if fast: 
            slow = slow.next
        while l and slow and l.val == slow.val:
            l,slow=l.next,slow.next
        return not l     

        
