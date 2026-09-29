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
            curr.random = copy_node
            curr = curr.next

        curr = head.random
        while curr:
            curr.next = curr.next.random if curr.next else None
            curr.random = curr.random.random if curr.random else None
            curr = curr.next
        return head.random