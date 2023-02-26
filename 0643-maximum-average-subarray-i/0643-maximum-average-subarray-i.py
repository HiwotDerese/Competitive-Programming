class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _sum, leng = 0, len(nums)
        for i in range(k):
            _sum += nums[i]
            
        _max = _sum
        left = 0
        
        for right in range(k, leng):
            _sum -= nums[left]
            _sum += nums[right]
            left += 1
            
            print(_max)
            _max = max(_max, _sum)
            
        
            
        return _max / k
            
        