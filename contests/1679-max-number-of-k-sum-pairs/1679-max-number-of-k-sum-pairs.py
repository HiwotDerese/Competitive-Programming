class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        leng = len(nums)
        sums = 0
        l = 0
        r = leng - 1
        ans = 0
        nums.sort()
        while l < r:
            if nums[l] + nums[r] < k:
                l += 1
            elif nums[l] + nums[r] > k:
                r -= 1
            else:
                ans += 1
                l += 1
                r -= 1
                
        return ans
