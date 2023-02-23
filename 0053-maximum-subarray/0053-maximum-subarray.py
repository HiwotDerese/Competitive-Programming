class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        leng = len(nums)
        pre, _max = 0, -float('inf')
        
        for i in range(leng):
            if pre > 0:
                nums[i] = nums[i] + pre
                
            pre = nums[i]
            _max = max(_max, nums[i])
            
            
        return _max
                
            
    
            
        