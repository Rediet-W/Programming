# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftprev = dummy
        curr = dummy.next
        for i in range(left-1):
            leftprev = leftprev.next
            curr = curr.next

        prev = ListNode()
        for i in range(right-left + 1):
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        leftprev.next.next = curr
        leftprev.next = prev

        return dummy.next