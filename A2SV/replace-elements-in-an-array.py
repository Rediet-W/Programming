class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_index= {n:i for i,n in enumerate(nums)}
        for operation in operations:
            value, new_value = operation
            if value in num_index:
                index = num_index[value]
                nums[index] = new_value  
                num_index[new_value] = index 
                del num_index[value]
        return nums