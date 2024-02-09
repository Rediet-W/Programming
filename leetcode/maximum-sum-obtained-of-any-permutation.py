class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        p = [0]* (n)
        
        #create an array p with the number of times that num[i] is going to be added
        for s,e in requests:
            p[s] += 1
            if e + 1<n:
                p[e+1] -=1

        # calc the prefix sum
        prefix = 0
        for i in range(n):
            prefix += p[i]
            p[i] = prefix 

        nums.sort()
        p.sort()

        # calculate the total sum of requests
        request_sum = 0
        for i in range(n):
            request_sum += (nums[i] * p[i]) 
        return request_sum%(10**9 + 7)
        


            
        