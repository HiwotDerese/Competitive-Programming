class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            x = [int(a) for a in str(nums[i])]
            for j in range(i + 1, len(nums)):
                y = [int(a) for a in str(nums[j])]
                if (x[0] < y[0]):
                    nums[i], nums[j] = nums[j], nums[i]
                elif x[0] == y[0]:
                    
                    if (x[1] < y[1]):
                        nums[i], nums[j] = nums[j], nums[i]
        answer = ''.join(map(str, nums))
        return answer
                