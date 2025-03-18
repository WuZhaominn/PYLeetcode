class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return
        dic = {}
        node = head
        #键（key）是原节点，值（value）是新节点
        while node:
            dic[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            dic[node].next = dic.get(node.next)
            dic[node].random =dic.get(node.random)
            node = node.next
        return dic[head]
