class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        ans = 0
        prefix_sum = 0
        col = {0:1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            diff = prefix_sum - k
            if diff in col:
                ans += col.get(diff)
                col[prefix_sum] = 1 + col.get(prefix_sum,0)
            else:
                col[prefix_sum] = 1 + col.get(prefix_sum,0)
        return ans
            