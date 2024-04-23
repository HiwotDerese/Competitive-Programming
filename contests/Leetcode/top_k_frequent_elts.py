class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        count = 0
        output = []
        for i in range(len(nums)):
            if i == 0:
                count += 1
            else:
                if nums[i] == nums[i - 1]:
                    count += 1
                elif count >= k:
                    output.append(nums[i - 1])
                    count = 1
        if count >= k:
            output.append(nums[i])
        if len(output) == 0:
            return nums
        return output
                    
                    
                    
            