# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        i, n = 0, len(nodes)
        for i in range(n // 2):
            nodes[i].next = nodes[n - 1 - i]
            nodes[n - 1 - i].next = nodes[i + 1]
        if i + 1 < n:
            nodes[i + 1].next = None