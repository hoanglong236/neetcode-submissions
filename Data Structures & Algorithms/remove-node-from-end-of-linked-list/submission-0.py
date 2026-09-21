# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev_target = None
        target = head
        target_idx = 0
        cur = head
        cur_idx = 0
        while cur:
            cur = cur.next
            cur_idx += 1
            if cur_idx - target_idx > n:
                prev_target = target
                target = target.next
                target_idx = 0
        if prev_target:
            prev_target.next = target.next
        else:
            head = head.next
        return head