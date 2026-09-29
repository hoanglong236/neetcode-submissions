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
        if head is None:
            return None

        curr = head
        while curr is not None:
            copy_node = Node(curr.val, curr.next)
            curr.next = copy_node
            curr = curr.next.next
        
        curr = head
        while curr is not None:
            copy_node = curr.next
            if curr.random is not None:
                copy_node.random = curr.random.next
            curr = curr.next.next
        
        copy_head = head.next
        curr = head
        while curr is not None:
            copy_node = curr.next
            curr.next = copy_node.next
            if curr.next is not None:
                copy_node.next = curr.next.next
            curr = curr.next

        return copy_head