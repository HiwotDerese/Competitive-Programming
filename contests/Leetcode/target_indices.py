class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        indices = []
        for i in range(len(nums)):
            for j in range((i + 1) , len(nums)):
                if nums[i] > nums[j]:
                    nums[i] , nums[j] = nums[j] , nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                indices.append(i)
            elif nums[i] > target:
                break
        return indices