# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = 0
        curr = head
        while f!= n:
            f+=1
            curr = curr.next
        newcurr = head
        if curr == None:
            return newcurr.next
        while curr.next:
            newcurr = newcurr.next
            curr = curr.next
        newcurr.next = newcurr.next.next if newcurr.next else None
        return head
