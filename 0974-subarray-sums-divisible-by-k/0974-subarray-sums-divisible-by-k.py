class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        leng = len(nums)
        modD, ans = {0:1}, 0
        
        pre_sum = 0
        for i in range(leng):
            nums[i] += pre_sum
            pre_sum = nums[i]
            mod = nums[i] % k
            print(mod)
            
            if mod in modD:
                ans += modD[mod]
                
            modD[mod] = 1 + modD.get(mod, 0)
                
                
        return ans