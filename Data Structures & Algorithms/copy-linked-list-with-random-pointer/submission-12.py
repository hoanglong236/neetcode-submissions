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

        curr = head
        while curr:
            copy_node = Node(curr.val, curr.next, curr.random)
            curr.next = copy_node
            curr = curr.next.next

        copy_head = head.next
        curr = head
        while curr:
            copy_node = curr.next
            copy_node.random = copy_node.random.next if copy_node.random else None
            curr = curr.next.next

        curr = head
        while curr:
            copy_node = curr.next
            curr.next = copy_node.next
            copy_node.next = copy_node.next.next if copy_node.next else None
            curr = curr.next

        return copy_head