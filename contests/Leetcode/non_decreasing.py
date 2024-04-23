# def non_decreasing(increasing, candidates, ans):
#         if not candidates:
#             increasing = increasing[:1]
#             return 
        
#         for i in range(len(candidates)):
#             # print(increasing, i, candidates)
#             if candidates[i] >= increasing[-1]:
#                 increasing.append(candidates[i])
#                 arr = increasing.copy()
#                 ans.append(arr)
#                 # print(candidates[1:])
#                 non_decreasing(increasing, candidates[i + 1:], ans)

#                 increasing.pop()
#         return

# def findSubsequences(nums):
#     if len(nums) < 2:
#         return []
    
#     ans, increasing, candidates = [], [nums[0]], nums[1:]
    
#     for i in nums:
#         print(ans)
#         non_decreasing(increasing, candidates, ans)
        
#     return ans

# print(findSubsequences([4,6,7,8]))


