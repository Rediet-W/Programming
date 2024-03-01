class ListNode:
    def __init__(self, prev = None, nxt = None, val= 0):
        self.prev = prev
        self.nxt = nxt
        self.val = val

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.left = ListNode()
        self.right = ListNode(self.left, None, 0)
        self.left.nxt = self.right


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(self.right.prev, self.right, value)
        self.right.prev.nxt = curr 
        self.right.prev = curr
        self.size -=1 
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.left.nxt = self.left.nxt.nxt
        self.left.nxt.prev = self.left
        self.size += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right

    def isFull(self) -> bool:
        return self.size == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()