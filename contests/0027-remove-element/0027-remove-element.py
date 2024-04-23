class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        for x in nums:
            if x != val:
                print(i)
                nums[i] = x
                i += 1
                
        return i
    