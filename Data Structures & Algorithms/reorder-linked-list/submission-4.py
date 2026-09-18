# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur, size = head, 0
        while cur:
            cur = cur.next
            size += 1

        cur, pivot = head, size // 2
        for _ in range(pivot):
            cur = cur.next

        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        cur, nxt = head, prev
        while cur:
            tmp = cur.next
            cur.next = nxt
            if nxt:
                tmp2 = nxt.next
                nxt.next = tmp
                nxt = tmp2
            cur = tmp