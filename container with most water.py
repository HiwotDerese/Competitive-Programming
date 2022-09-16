class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = []
        n = len(height)
        right = n-1
        i = 0
        while i < right:
            # while height[i] > height[right]:
            #     right -= 1
            ans.append((right-i) * min(height[i], height[right]))
            if height[i] < height[right]:
                i += 1
            else:
                right -=1
        return max(ans)
            
         