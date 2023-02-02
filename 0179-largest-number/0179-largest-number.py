class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(len(nums), 0, -1):
            for j in range(i-1):
                
                if not str(nums[j]) + str(nums[j+1]) > str(nums[j+1]) + str(nums[j]):
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    
        return str(int("".join(map(str, nums))))

        # def compare(self, n1, n2):
        #     return str(nums[j]) + str(nums[j+1]) > str(nums[j+1]) + str(nums[j])