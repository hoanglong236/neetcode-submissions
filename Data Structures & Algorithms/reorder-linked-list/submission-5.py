# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev_slow, slow = None, head
        fast = head
        while fast:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next if fast.next else None
        prev_slow.next = None

        cur, prev = slow, None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        first, second = head, prev
        while first:
            first_next = first.next
            if second:
                first.next = second
                second_next = second.next
                second.next = first_next
                second = second_next
            first = first_next