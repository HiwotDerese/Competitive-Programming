class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans1 = [1] * len(nums)
        ans2 = [1] * len(nums)
        ans = [1] * len(nums)
        pre_sum = 1
        post_sum = 1
        for i in range(len(nums)):
            ans1[i] = pre_sum
            pre_sum *= nums[i]
        for j in range(len(nums)):
            ans2[-(j+1)] = post_sum
            post_sum *= nums[-(j+1)]
            ans[-(j+1)] = ans1[-(j+1)] * ans2[-(j+1)]
        return ans
            
            
        
        
            
        