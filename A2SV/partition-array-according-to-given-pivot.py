class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        more = []
        between = []
        for i in range(len(nums)):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])
            else:
                between.append(pivot)
        pivoted = less + between + more
        return pivoted