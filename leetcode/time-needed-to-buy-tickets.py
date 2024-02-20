class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = []
        for i in range(n):
            queue.append(i)
        count = 0
        while len(queue) != 0:
            count+=1
            front = queue.pop(0)
            if tickets[front] >= 1:
                tickets[front] -= 1
            if k == front and tickets[front] == 0:
                break
            if k!= front and tickets[front] == 0:
                continue
            queue.append(front)

        return count
            