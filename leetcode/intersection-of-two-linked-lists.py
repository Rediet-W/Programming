# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dictt = {}
        curr = headA
        while curr:
            dictt[curr] = 0
            curr = curr.next
        
        curr2 = headB
        while curr2:
            if curr2 in dictt:
                return curr2
            curr2 = curr2.next
        return None