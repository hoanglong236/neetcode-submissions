"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        dummy = Node(0, Node(0))

        curr = head
        copy_node = dummy.next
        random_map = {curr: copy_node}
        while curr:
            copy_node.val = curr.val
            if curr.next:
                copy_node.next = random_map.setdefault(curr.next, Node(0))
            if curr.random:
                copy_node.random = random_map.setdefault(curr.random, Node(0))
            copy_node = copy_node.next
            curr = curr.next
        return dummy.next