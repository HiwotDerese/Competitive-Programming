class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        pre = [0]
        for num in nums:
            pre.append(pre[-1]+num)
        # print(pre)
        # arr = [nums[0]]
        # for i in range(1,len(nums)):
        #     arr.append(nums[i] + arr[i - 1])
            
        deque = collections.deque()
        # print(deque)
        result = len(nums) + 1
        # print(result)
        for i in range(len(pre)):
            while(deque and deque[-1][1] >=pre[i]):
                deque.pop()
            while deque and pre[i] - deque[0][1] >= K:
                # print(result)
                result = min(i-deque[0][0], result)
                # print(result)
                deque.popleft() 
            deque.append([i,pre[i]])
            # print(deque)
        return result if result < (len(nums) + 1) else -1           