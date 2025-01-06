
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if not head:
            slow, fast = None, None
        else:
            slow, fast = head, head.next
        while slow != None and fast != None:
            if slow == fast:
                return True
            if not fast.next:
                slow, fast = None, None 
            else:
                slow, fast = slow.next, fast.next.next 
        return False
