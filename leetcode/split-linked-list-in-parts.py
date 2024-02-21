# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        #find the length
        dummy = ListNode()
        dummy.next = head
        n = 0
        while dummy.next:
            n+=1
            dummy = dummy.next
        
        #now divide the first only 
        each = n // k 
        first = n % k  # for the _ we will have extra one
        ans = []
        prev = None
        curr = head
        for i in range(k):
            ans.append(curr)
            for _ in range(each):
                if curr:
                    prev = curr
                    curr = curr.next 

            if first and curr:
                prev = curr
                curr = curr.next
                first-=1
            if prev:
                prev.next = None
            
        return ans
