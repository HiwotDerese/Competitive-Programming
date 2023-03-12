class Solution:
    
    def uniqueSubsets(self, nums, ans):
        if not nums:
            return ans
        
        candidates = ans.copy()
        for i in candidates:
            ans.append([nums[-1]] + i)
        
        ans.append([nums[-1]])
        nums.pop()
        # print(ans, nums)
        # print(ans)
        self.uniqueSubsets(nums, ans)
        
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        self.uniqueSubsets(nums, ans)
        
        return [[]] + ans
        
         
        