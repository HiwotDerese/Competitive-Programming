class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans, leng1, leng2 = 0, len(nums), len(requests)
            
        arr = [0] * (len(nums) + 1)
        
        for i in range(leng2):
            arr[requests[i][0]] += 1
            arr[requests[i][1] + 1] -= 1
            
        pre_sum = 0
        for i in range(len(arr)):
            arr[i] += pre_sum
            pre_sum = arr[i]
            
        arr.sort()
        nums.sort()

        for i in range(leng1):
            ans += (arr[i + 1] * nums[i])
            
        return ans % 1000000007
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        