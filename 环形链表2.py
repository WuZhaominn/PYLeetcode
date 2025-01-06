
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        
        if not head:
            return None
        slow, fast = head,head
        while fast and fast.next :
            slow, fast = slow.next, fast.next.next 
            if slow == fast:
                slow=head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None
