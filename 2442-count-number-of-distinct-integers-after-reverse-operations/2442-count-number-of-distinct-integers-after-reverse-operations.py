class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        unique = set(nums)
        
        for i in nums:
            strg = str(i) 		
            reverse_strg = strg[::-1] 
            unique.add(int(reverse_strg))
        
        return len(unique)
    