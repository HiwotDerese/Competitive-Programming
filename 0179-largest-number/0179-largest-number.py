class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        leng = len(nums)
        for i in range(leng, 0, -1):
            
            for j in range(i-1):
                
                num1 = str(nums[j]) + str(nums[j+1])
                num2 = str(nums[j+1]) + str(nums[j])
                
                if num1 < num2:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        for i in range(leng):
            nums[i] = str(nums[i])
        
        ans = "".join(nums)
        ans = str(int("".join(nums)))
        
        return ans