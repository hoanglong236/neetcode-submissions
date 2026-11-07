class Node:
    def __init__(self, key=0, val=0, freq=0, left=None, right=None):
        self.key = key
        self.val = val
        self.freq = freq
        self.left = left
        self.right = right

class LFUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.node_map = {}
        self.freq_last_recently_map = {}
        self.cap = capacity

    def _remove_current_pos(self, node) -> None:
        left, right = node.left, node.right
        if self.freq_last_recently_map[node.freq] == node:
            if left.freq == node.freq:
                self.freq_last_recently_map[node.freq] = left
            else:
                del self.freq_last_recently_map[node.freq]
        left.right = right
        right.left = left
    
    def _append_at_last_of_frequently_used(self, node) -> None:
        node.freq += 1
        freq = node.freq
        while freq > 0 and freq not in self.freq_last_recently_map:
            freq -= 1
        if freq > 0:
            last = self.freq_last_recently_map[freq]
            right = last.right
            last.right = node
            node.left = last
            right.left = node
            node.right = right
        else:
            head_right = self.head.right
            self.head.right = node
            node.left = self.head
            node.right = head_right
            head_right.left = node
        self.freq_last_recently_map[node.freq] = node
    
    def _pop_lfu_lru(self):
        least = self.head.right
        if least is self.tail:
            return
        del self.node_map[least.key]
        self._remove_current_pos(least)

    def get(self, key: int) -> int:
        node = self.node_map.get(key)
        if node is None:
            return -1
        self._remove_current_pos(node)
        self._append_at_last_of_frequently_used(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.node_map.get(key)
        if node is None:
            node = Node(key, value)
            self.node_map[key] = node
            if self.cap == 0:
                self._pop_lfu_lru()
            else:
                self.cap -= 1
        else:
            node.val = value
            self._remove_current_pos(node)
        self._append_at_last_of_frequently_used(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)