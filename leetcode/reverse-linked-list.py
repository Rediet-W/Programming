# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        if curr == None:
            return head
        nxt = curr.next
        prev = None
        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = curr.next if curr else None
        head == curr
        if curr == None:
            head = prev
        return head