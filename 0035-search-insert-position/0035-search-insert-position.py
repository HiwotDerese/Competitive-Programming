class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
         if target>nums[-1]:
            return len(nums)

         return bisect_left(nums,target,0,len(nums)-1)
        
        
        
        
        
#         if target in nums:
#             return nums.index(target)
#         else:
#             for i in nums:
#                 if i > target:
#                     return nums.index(i)
#         return len(nums)
        