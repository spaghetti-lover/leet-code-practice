# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return head

        while head is not None and head.val == val:
            head = head.next
        new_head = head

        while head is not None and head.next is not None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return new_head
