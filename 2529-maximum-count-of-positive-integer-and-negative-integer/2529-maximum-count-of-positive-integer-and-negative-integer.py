class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        leng = len(nums)
        pos_count = 0
        neg_count = 0
        for i in range(leng):
            
            if nums[i] < 0:
                neg_count +=1 
                
            elif nums[i] > 0:
                pos_count += 1
            
        return max(pos_count, neg_count)
    
        