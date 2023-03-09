class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
#         def backtrack(num, candidate, k, ans):
            
#             if len(candidate) == k - 1:
#                 comb = candidate
#                 comb.insert(0, num)
#                 # print('aaaaa')
#                 ans.append(comb)
#                 # print(ans)
#                 return 
                
                
#             for i in range(len(candidate)):
#                 print(candidate, 'candidate', num)
#                 if len(candidate) >= k:
#                     backtrack(candidate[i], candidate[i+1:], k, ans)
                    
        
#         ans = []
#         arr = []
        
#         for i in range(n):
#             arr.append(i + 1)
            
#         backtrack(arr[0], arr[1:], k, [])
        
#         return ans
        
        
        
        
        
        
        
        
        
        
        
        
        ans = []

        def helper(combination, start, remaining_slots):
            if remaining_slots == 0:
                ans.append(combination)
                
            else:
                for num in range(start, n + 1):
                    helper(combination + [num], num + 1, remaining_slots - 1)
                    
            # print(ans)

        helper([], 1, k)

        return ans
    
    
    
    