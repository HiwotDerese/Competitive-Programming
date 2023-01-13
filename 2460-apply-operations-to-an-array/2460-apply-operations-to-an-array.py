class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        i = 0
        count = 0

        while count < leng - 1:

            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                
            else:
                
                if nums[i] == nums[i + 1]:
                    nums[i] += nums[i]
                    nums.pop(i + 1)
                    nums.append(0)
                    
                i += 1
            count += 1

        return nums
        