class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)
        # print(small, large)
        def gcd(small, large):
            
            if large == 0:
                return small
            
            return gcd(large, small % large)
        
        return gcd(small, large)
        
        
        
        
        
        