class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
        processorTime.sort()
        mx=0        
        for i in range(len(processorTime)):
            mx = max(mx, processorTime[i] + tasks[i*4])
        return mx