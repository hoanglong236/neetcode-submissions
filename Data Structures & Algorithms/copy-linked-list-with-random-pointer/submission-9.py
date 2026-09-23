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
        dummy = Node(0, Node(head.val))

        curr = head
        copy_node = dummy.next
        nodes_map = {curr: copy_node}
        while curr:
            if curr.next:
                if curr.next in nodes_map:
                    copy_node.next = nodes_map[curr.next]
                else:
                    copy_node.next = Node(curr.next.val)
                    nodes_map[curr.next] = copy_node.next
            if curr.random:
                if curr.random in nodes_map:
                    copy_node.random = nodes_map[curr.random]
                else:
                    copy_node.random = Node(curr.random.val)
                    nodes_map[curr.random] = copy_node.random
            copy_node = copy_node.next
            curr = curr.next
        return dummy.next