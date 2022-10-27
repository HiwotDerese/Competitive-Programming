class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        queue = [0]
        arr = [nums[0]]
        for i in range(1, len(nums)):
            while queue and queue[0] < (i - k): # if we reached k size
                queue.pop(0)     
            arr.append(nums[i] + arr[queue[0]])
            while queue and arr[i] >= arr[queue[-1]]: 
                queue.pop()
            queue.append(i)
        return arr[-1]

# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         dq: Deque[int] = collections.deque([nums[0]])

#         for num in nums[1:]:
#             dq.append(dq[0] + num)

#             while len(dq) > k or (len(dq) > 1 and dq[0] <= dq[-1]):
#                 dq.popleft()
#         if dq[-1] < nums[0]:
#             return nums[0]
#         return dq[-1]


# class Solution:
#     def maxResult(self, nums: List[int], k: int) -> int:
#         arr = [nums[0]]
#         indx = [0]
#         for i in nums[1:]:
#             arr.append(arr[0] + i)
#             indx.append(i)
#             while (len(arr) > k) or (arr[0] <= arr[-1] and len(arr) > 1):
#                 arr.pop(0)
#         # if arr[-1] < nums[0]:
#         #     return nums[0]
#         return arr[-1]
            
                

