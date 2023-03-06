class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        leng, _sum, ans,left, dic = len(nums), 0, 0,0,{0:1}
        
        for i in range(leng):
            _sum += nums[i]
            diff = _sum - goal
            
            if diff in dic:
                ans += dic.get(diff)
                
            dic[_sum] = 1 + dic.get(_sum, 0)
            
        return ans

            