class Solution:
    
    def non_decreasing(self, increasing, candidates, ans):
        if not candidates:
            return 
        
        for i in range(len(candidates)):
            # print(increasing, i, candidates)
            if candidates[i] >= increasing[-1]:
                increasing.append(candidates[i])
                arr = increasing.copy()
                ans.add(tuple(arr))
                # print(candidates[1:])
                self.non_decreasing(increasing, candidates[i + 1:], ans)

                increasing.pop()
        return ans
        
    
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []
        
        ans, increasing, candidates = set(), [nums[0]], nums[1:]
        
        for i in range(len(nums)):
            
            self.non_decreasing([nums[i]], nums[i + 1:], ans)
            
        return list(ans)
        
        
        