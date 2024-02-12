class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None      

    def get(self, index: int) -> int:
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy.next
        
        while index > 0 and curr:
            curr = curr.next
            index-=1
        return curr.val if curr else -1
        

        

    def addAtHead(self, val: int) -> None:
        '''Newnode = Node(val)
        dummy = Node(0)
        dummy.next = self.head
        Newnode.next = self.head
        dummy.next = Newnode
        self.head = Newnode'''
        self.addAtIndex(0,val)
 


    def addAtTail(self, val: int) -> None:
        dummy = Node(0)
        dummy.next = self.head
        newNode = Node(val)
        curr = dummy
        while curr.next:
            curr = curr.next
        curr.next = newNode 
        self.head = dummy.next

    def addAtIndex(self, index: int, val: int) -> None:
        dummy = Node(0)
        dummy.next = self.head
        Newnode = Node(val)
        curr = dummy
        while curr and index > 0:
            curr= curr.next
            index-= 1
        if curr:
            Newnode.next = curr.next
            curr.next = Newnode
        self.head = dummy.next

    def deleteAtIndex(self, index: int) -> None:
        dummy = Node(0)
        dummy.next = self.head
        curr = dummy
    
        while index > 0 and curr:
            curr = curr.next 
            index-=1
        if curr:
            curr.next = curr.next.next if curr.next else None
        self.head = dummy.next
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)