class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''prefix = [0] * capacity

        for n, f, t in trips:
            if f - 1 < capacity:
                prefix[f-1] += n
            if t< capacity:
                prefix[t] -= n

        curr = 0
        for i in range(capacity):
            curr += prefix[i]
            prefix[i] = curr

        for i in prefix:
            if i > capacity:
                return False
        return True'''

        ls = []
        for n, f, t in trips:
            ls.append((f,n,1))
            ls.append((t,n,0))

        ls.sort(key = lambda x: (x[0], x[2]))

        curr = 0
        for t, p, i in ls:
            if i:
                curr += p
            else:
                curr -= p
            if curr > capacity:
                return False
        return True


