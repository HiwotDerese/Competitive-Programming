class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        leng = len(nums)
        
        greater = []
        less = []
        equal = []
        
        for i in range(leng):
            if nums[i] > pivot:
                greater.append(nums[i])
                
            elif nums[i] < pivot:
                less.append(nums[i])
                
            else:
                equal.append(nums[i])
        
        ans = less + equal + greater
        
        return ans
        
        
        