class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        summ = 0
        prefix_arr = []
        for i in range(len(self.nums)):
            summ += self.nums[i]
            prefix_arr.append(summ)
        if left > 0:
            return prefix_arr[right] - prefix_arr[left-1]
        else:
            return prefix_arr[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)