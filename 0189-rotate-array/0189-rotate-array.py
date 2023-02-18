class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leng = len(nums)
        i = 0
        k = k % leng
        j = leng - k - 1
        for _ in range(2):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            i = leng - k
            j = leng - 1
        nums.reverse()
            
        
            
        