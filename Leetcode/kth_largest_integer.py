class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i in range(len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if nums[j - 1] > nums[j]:
                        nums[j - 1], nums[j] = nums[j],nums[j - 1]
        return nums[-k]