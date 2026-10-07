# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if right - left == 0:
            return head

        dummy = ListNode()
        dummy.next = head
        prev, curr, idx = None, head, 1
        while curr is not None:
            if idx == left:
                break
            prev = curr
            curr = curr.next
            idx += 1

        prev_sub_head, sub_head = prev, curr

        while curr is not None:
            if idx > right:
                break
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
            idx += 1

        if prev_sub_head is None:
            dummy.next = prev
        else:
            prev_sub_head.next = prev
        sub_head.next = curr

        return dummy.next