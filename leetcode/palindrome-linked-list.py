# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        ls = []
        while curr:
            ls.append(curr.val)
            curr = curr.next
        n = len(ls) - 1
        i =0
        while i < n:
            if ls[i] != ls[n]:
                return False
            i += 1
            n-=1
        return True
