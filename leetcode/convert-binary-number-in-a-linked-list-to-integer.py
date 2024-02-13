# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        ans = 0
        n = 0
        while curr:
            n +=1
            curr = curr.next
        curr = head
        for i in range(n):
            s = curr.val
            ans += s*(2**(n-i-1))
            curr = curr.next
        return ans

        