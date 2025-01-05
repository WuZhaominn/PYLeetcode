class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        #交点
        ans = None
        while a or b:
            if not a:
                a = headB
            if not b:
                b = headA
            #检查交点
            if a == b and not ans:
                ans = a
            a, b = a.next, b.next
        return ans
        
