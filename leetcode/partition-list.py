# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyl = ListNode()
        dummyr = ListNode()
        less = dummyl
        more = dummyr
        curr = head
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next            
            else:
                more.next = curr
                more = more.next
            curr = curr.next

        less.next = dummyr.next
        more.next = None
        return dummyl.next