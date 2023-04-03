class Solution:
    def maxOr(self, nums, subset, dic):
        
        if not nums:
            return
        
        for i in range(len(nums)):
            subset.append(nums[i])
            
            ans = reduce(lambda x, y: x | y, subset)
            
            dic[ans] = 1 + dic.get(ans, 0)
            
            self.maxOr(nums[i+1:], subset, dic)
            subset.pop()
            
        return dic
            
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        self.dic = {}
        
        self.maxOr(nums, [], self.dic)
        s = dict(sorted(self.dic.items(), key=lambda item: item[1]))
        idx = list(s)[-1]
        
        return self.dic[idx]
    
    
    
    
        
        
        
        
        
                                                                                                                                                                                               