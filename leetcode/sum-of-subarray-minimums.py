class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        prefix = [(0,-1)]
        p = [0] * len(arr)
        for i in range(len(arr)):
            while prefix[-1][0] > arr[i]:
                prefix.pop()
            p[i] = i- prefix[-1][1] 
            prefix.append((arr[i], i))
            
        suffix = [(0,len(arr))]
        s = [0] * len(arr)
        for i in range(len(arr)-1, -1, -1):
            while suffix[-1][0] >= arr[i]:
                suffix.pop()
            s[i] = suffix[-1][1] - i 
            suffix.append((arr[i], i))
        
        total = []
        for i in range(len(arr)):
            curr = p[i] * s[i]
            total.append(arr[i] * curr) 
        
        return sum(total) % (10**9 + 7)

        