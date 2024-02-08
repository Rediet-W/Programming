class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n
        for f,l,s in bookings:
            prefix[f-1] += s
            if l < n:
                prefix[l] -= s

        curr = 0
        for i in range(n):
            curr += prefix[i]
            prefix[i] = curr
        
        return prefix