class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        print(q)    
        ans.append(nums[q[0]])
        
        left = 0
        
        for right in range(k, len(nums)):
            while q and nums[right] > nums[q[-1]]:
                q.pop()
            q.append(right)
            
            if q[0] == left:
                q.popleft()
            left += 1
                
            ans.append(nums[q[0]])
            
        return ans
            
        
        
        