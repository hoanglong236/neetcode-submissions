class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dummy_head = Node()
        self.dummy_last = Node()
        self.dummy_head.next = self.dummy_last
        self.dummy_last.prev = self.dummy_head
        self.nodes = {}
    
    def pop_least_used(self):
        head = self.dummy_head.next
        if head == self.dummy_last:
            return
        next_head = head.next
        self.dummy_head.next = next_head
        next_head.prev = self.dummy_head
        head.next, head.prev = None, None
        head.val = -1
    
    def put_most_used(self, node):
        last_node = self.dummy_last.prev
        last_node.next = node
        node.prev = last_node
        node.next = self.dummy_last
        self.dummy_last.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        if node.val == -1:
            return -1
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        last_used_node = self.dummy_last.prev
        if last_used_node != node:
            self.put_most_used(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes:
            if self.size == self.capacity:
                self.pop_least_used()
            else:
                self.size += 1
            node = Node(key, value, None, None)
            self.put_most_used(node)
            self.nodes[key] = node
        else:
            node = self.nodes[key]
            if node.val == -1:
                if self.size == self.capacity:
                    self.pop_least_used()
                else:
                    self.size += 1
            else:
                prev_node, next_node = node.prev, node.next
                prev_node.next, next_node.prev = next_node, prev_node
            node.val = value
            self.put_most_used(node)