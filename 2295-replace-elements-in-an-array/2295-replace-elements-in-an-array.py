class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        len_nums = len(nums)
        len_op = len(operations)
        dic = {}
        
        for i in range(len_nums):
            dic[nums[i]] = i
            
        for i in range(len_op):
            num = operations[i][0]
            index = dic[num]
            
            nums[index] = operations[i][1]
            dic[operations[i][1]] = index
            
        return nums
        