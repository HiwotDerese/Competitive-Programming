class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxm = max(candies)
        ans = []
        for i in candies:
            with_extra = i + extraCandies
            if with_extra >= maxm:
                ans.append(True)
            else:
                ans.append(False)
        return ans
            
            
        