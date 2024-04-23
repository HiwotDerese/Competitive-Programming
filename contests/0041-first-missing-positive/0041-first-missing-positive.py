class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        def sortt(nums) -> int:
            idx = len(nums)

            index = 0
            while index < len(nums):
                if nums[index] == index + 1 or nums[index] < 1 or nums[index] >= len(nums):
                    index += 1
                elif nums[nums[index] - 1] == nums[index]:
                    index += 1

                else:
                    nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]

            return idx
        
        sortt(nums)
        n = len(nums)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
               
        
        