class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx = leng = len(nums)
        # nums.append(-1)
        
        index = 0
        while index < len(nums):
            # print(index, nums)
            if nums[index] == index + 1:
                index += 1
                
            elif nums[index] == 'first':
                index += 1
                
            elif nums[index] < 1 or nums[index] > leng:
                nums[index] = 'first'
                index += 1
                
            else:
                if nums[nums[index] - 1] == nums[index]:
                    nums[index] = 'first'
                    index += 1
                else:
                # print(index, nums[index], nums[nums[index] - 1])
                    nums[nums[index] - 1], nums[index] = nums[index], nums[nums[index] - 1]
                # if nums[index] == len(nums):
                #     idx = index
                # elif nums[nums[index]] == len(nums):
                #     idx = index
        
        for i in range(leng):
            if nums[i] == 'first':
                return i + 1
            
        return leng + 1
               
        
        