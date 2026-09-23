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
        dummy = Node(0)
        copy_node = Node(0)
        dummy.next = copy_node

        curr = head
        instance_map = {}
        while curr:
            copy_node.val = curr.val
            copy_node.next = Node(0) if curr.next else None
            instance_map[curr] = copy_node
            copy_node = copy_node.next
            curr = curr.next

        copy_node = dummy.next
        curr = head
        while curr:
            if curr.random:
                copy_node.random = instance_map[curr.random]
            curr = curr.next
            copy_node = copy_node.next
        return dummy.next
        