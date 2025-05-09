class ListNode:
    #定义双向链表
    def __init__(self,key=0,val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity =capacity
        self.hashmap={}
        self.head = ListNode()
        self.tail =ListNode()
        self.head.next =self.tail
        self.tail.prev =self.head

    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def add_node_to_last(self,node):
        self.tail.prev.next=node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev =node
    def move_node_to_last(self,node):
        self.remove_node(node)
        self.add_node_to_last(node)

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1
        else:
            node = self.hashmap[key]
            self.move_node_to_last(node)
            return node.val
    def put(self, key: int, value: int) -> None:
        if key not in self.hashmap:
            if len(self.hashmap)==self.capacity:
                del self.hashmap[self.head.next.key]
                self.remove_node(self.head.next)
            node =ListNode( key,value)
            self.hashmap[key]=node
            self.add_node_to_last(node)
            
        else:
            node = self.hashmap[key]
            node.val=value
            self.move_node_to_last(node)
            return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
