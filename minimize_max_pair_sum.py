class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxm = 0
        n = len(nums)//2
        for i in range(n):
            ans = max(maxm, nums[i] + nums[-(i+1)])
            maxm = ans
        return ans