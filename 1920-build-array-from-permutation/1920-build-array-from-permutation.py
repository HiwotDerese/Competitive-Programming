class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        leng = len(nums)
        
        for i in range(leng):
            index = nums[i]
            ans.append(nums[index])
        
        return ans
        