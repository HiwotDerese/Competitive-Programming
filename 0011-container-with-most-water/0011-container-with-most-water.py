class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        right = n-1
        left = 0
        while left < right:
            water = (right-left) * min(height[left], height[right])
            ans = max(ans, water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        return ans
            
         