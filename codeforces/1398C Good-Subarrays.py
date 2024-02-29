from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ls = []
    for i in range(n):
        ls.append(int(s[i]))
    prefix_sum = 0
    count_prefix_sum = defaultdict(int) # Initialize with prefix sum 0 occurring once
    good_subarrays = 0
    count_prefix_sum[1] = 1
    
    for i in range(len(ls)):
        prefix_sum += ls[i]
        diff = prefix_sum - (i)
        if diff in count_prefix_sum:
            good_subarrays += count_prefix_sum[diff]
        count_prefix_sum[diff] +=  1
    print(good_subarrays)

 
