class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num = sorted(nums)
        print(num)
        ans = 0
        i = 0
        while i < len(nums):
            print(num[i])
            ans += num[i]
            # print(ans)
            i += 2
        return ans