class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # find max n times o(n) then flipping O(n)
        # find max value , idx then flip till arr[k-1] flip arr[n-1] appendk,n to result use two pointers

        def flip(end):
            start = 0
            while start< end:
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
            

        l = len(arr)
        answer = []
        for i in range(l-1,-1,-1):
            ma = i
            for j in range(i,-1,-1):
                if arr[j]> arr[ma]:
                    ma= j
            if ma != i:
                flip(ma)
                flip(i)
                answer.append(ma +1)
                answer.append(i+1)
        return answer
