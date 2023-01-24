class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        holder = 0
        seeker = 0
        while seeker < leng:
            if nums[seeker] == 0:
                seeker += 1
            else:
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                seeker += 1
                holder += 1
                
        return nums
        # i = 0
        # j = 0
        # while i < len(nums):
        #     if nums[j] == 0:
        #         nums.append(0)
        #         nums.pop(j)
        #     else:
        #         j += 1
        #     i += 1
                
        
        