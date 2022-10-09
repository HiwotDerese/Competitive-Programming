class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        while i < k:
            nums.insert(0,nums[j])
            i += 1
            nums.pop()

        
            
