class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = {}
        left = 0
        ans = 0
        for right in range(n):
            if s[right] not in seen:
                ans = max(ans, right - left + 1)
            else:
                if seen[s[right]] < left:
                    ans = max(ans,right - left + 1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
        return ans
    