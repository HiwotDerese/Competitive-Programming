class Solution:
    def longestSubarray(self, nums, limit):
        minm  = []
        maxm = []
        ans = 0
        i = 0
        for j in range(len(nums)):
            while maxm and maxm[-1] < nums[j]:
                maxm.pop()
            while minm and minm[-1] > nums[j]:
                minm.pop()
            minm.append(nums[j])
            maxm.append(nums[j])
            if maxm[0] - minm[0] <= limit:
                ans = max(ans, j-i+1)
            else:
                if maxm[0] == nums[i]:
                    maxm.pop(0)
                if minm[0] == nums[i]:
                    minm.pop(0)
                i= i+ 1
        return ans
    
                    
                    
        