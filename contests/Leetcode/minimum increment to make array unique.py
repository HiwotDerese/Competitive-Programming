class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ans = 0
        j = -1
        nums.sort()
        for i in nums:
            if j < i:
                j = i
            else:
                level += 1
                ans += j - i
        
        return ans
        # stack = []
        # ans = 0
        # for i in range(len(nums)-1):
        #     stack.append(nums[0])
        #     nums.pop(0)
        #     while stack[-1] in nums:
        #         stack[-1] += 1
        #         ans += 1
        #     nums.append(stack.pop())
        # return ans
            