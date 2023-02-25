class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        leng = len(nums)
        _sum, _min, left = 0, float('inf'), 0
        
        for right in range(leng):
            _sum += nums[right]
            
            while _sum >= target:
                _min = min(_min, right - left + 1)
                _sum -= nums[left]
                left += 1
                
        
        if _min == float('inf'):
            return 0
        return _min
                
            
                
                
                
        
        