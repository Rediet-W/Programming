class Solution:
    def totalMoney(self, n: int) -> int:
        full_week = n//7
        rem = n % 7
        total_rem = 0
        total_full = 0

        for i in range(full_week+1, full_week + 1 +rem):
            total_rem +=i
        for j in range(full_week):
            start = j + 1
            end = j + 7
            for k in range(start, end + 1):
                total_full += k
        total = total_rem + total_full
        return total
        