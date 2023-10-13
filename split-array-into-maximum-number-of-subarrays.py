class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_ = nums[0]

        for num in nums:
            min_ = min_ & num

        count = 0
        curr = -1

        for num in nums:
            if curr == -1:
                curr = num
                
            curr = curr & num
            if curr == min_:
                count += 1
                curr = -1

        if (curr == -1 or min_ == 0) and count * min_ == min_:
            return count

        return 1