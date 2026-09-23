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

        curr = head
        nodes_map = {}
        while curr:
            copy_node = Node(curr.val)
            nodes_map[curr] = copy_node
            curr = curr.next

        dummy.next = nodes_map[head]
        curr = head
        copy_node = dummy.next
        while curr:
            if curr.next:
                copy_node.next = nodes_map[curr.next]
            if curr.random:
                copy_node.random = nodes_map[curr.random]
            curr = curr.next
            copy_node = copy_node.next
        return dummy.next