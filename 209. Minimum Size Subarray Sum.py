class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minm = len(nums) + 1
        i = 0
        j = 0
        sums = 0
        while i < len(nums) and j < len(nums):
            sums += nums[j]
            if sums < target:
                j += 1
            elif sums >= target:
                minm = min(minm, j - i + 1)
                while i <= j:
                    sums -= nums[i]
                    if sums >= target:
                        i += 1
                        minm = min(minm, j - i + 1)
                    else:
                        i += 1
                        j += 1
                        break
        
        return 0 if minm == len(nums) + 1 else minm 