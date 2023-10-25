class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m, ans = len(nums1), len(nums2), [0]
        dp = {}

        def dfs(i, j):
            if i == n or j == m:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            
            if nums1[i] == nums2[j]:
                ans[0] = 1 + dfs(i + 1, j + 1)
                

            else:
                ans[0] = max(dfs(i + 1, j), dfs(i, j + 1))
            
            dp[(i, j)] = ans[0]
            return ans[0]

        return dfs(0, 0)