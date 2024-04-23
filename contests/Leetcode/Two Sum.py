class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        for i in range(len(nums)):
            for j in range((i + 1),len(nums),1):
                if (nums[i] + nums[j] == target):
                    output.append(i)
                    output.append(j)
                    break
        return output

# ********************************************************************************************************
# two pointers method
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr2 = sorted(nums)
        l = 0
        r = len(nums) - 1
        ans = []
        while l < r:
            if arr2[l] + arr2[r] > target:
                r -= 1
            elif arr2[l] + arr2[r] < target:
                l += 1
            else:
                if nums.index(arr2[l])!= nums.index(arr2[r]):
                    ans.append(nums.index(arr2[l]))
                    ans.append(nums.index(arr2[r]))
                else:
                    ans.append(nums.index(arr2[l]))
                    ans.append(nums[l+1:].index(arr2[r])+l+1)
                break
        return ans
