# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        remainder = 0

        while l1 and l2:
            node = ListNode(0)
            remainder, node.val = divmod(l1.val + l2.val + remainder, 10)
            l1 = l1.next
            l2 = l2.next
            curr.next = node
            curr = curr.next
        while l1:
            node = ListNode(0)
            remainder, node.val = divmod(l1.val + remainder, 10)
            l1 = l1.next
            curr.next = node
            curr = curr.next
        while l2:
            node = ListNode(0)
            remainder, node.val = divmod(l2.val + remainder, 10)
            l2 = l2.next
            curr.next = node
            curr = curr.next
        if remainder:
            node = ListNode(remainder)
            curr.next = node
            curr = curr.next
        return dummy.next