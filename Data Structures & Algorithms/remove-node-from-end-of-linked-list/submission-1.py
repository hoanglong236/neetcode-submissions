# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        for _ in range(n):
            cur = cur.next
        prev_target, target = None, head
        while cur:
            cur = cur.next
            prev_target = target
            target = target.next
        if not prev_target:
            return head.next
        prev_target.next = target.next
        return head