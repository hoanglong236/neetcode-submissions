# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = ListNode()
        start.next = head
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        
        pivot = size // 2
        cur = head
        for _ in range(pivot):
            cur = cur.next

        prev = None
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        cur, next = head, prev
        # print(p1.val, p2.val)
        # while p1:
        #     print('p1 ', p1.val)
        #     p1 = p1.next
        # while p2:
        #     print('p2 ', p2.val)
        #     p2 = p2.next

        while cur:
            tmp = cur.next
            cur.next = next
            if next:
                tmp2 = next.next
                next.next = tmp
                next = tmp2
            cur = tmp
        # print(head.val, head.next)
        # return head