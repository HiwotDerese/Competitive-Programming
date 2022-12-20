class Solution:
  def maxFrequency(self, nums: List[int], k: int) -> int:
    nums.sort()
    ans = 0
    sum = 0
    count = 0
    for i in range(len(nums)):
      sum += nums[i]
      while sum + k < nums[i] * (i - count + 1):
        sum -= nums[count]
        count += 1
      ans = max(ans, i - count + 1)

    return ans